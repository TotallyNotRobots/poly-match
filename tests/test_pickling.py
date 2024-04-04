import itertools
import pickle
from typing import Any, TypeVar, cast

import pytest

import polymatch
from polymatch import pattern_registry
from polymatch.base import PolymorphicMatcher

patterns = ("regex::test", "exact::test", "contains:cf:test", "glob::beep")


class C:
    def __init__(self, pat: PolymorphicMatcher[Any, Any]) -> None:
        self.patterns = [pat]


T = TypeVar("T")


def cycle_pickle(obj: T, proto: int) -> T:
    return cast(T, pickle.loads(pickle.dumps(obj, proto)))


@pytest.mark.parametrize(
    ("pattern", "pickle_proto"),
    itertools.product(patterns, range(pickle.HIGHEST_PROTOCOL + 1)),
)
def test_compile_state(pattern: str, pickle_proto: int) -> None:
    compiled_pattern = pattern_registry.pattern_from_string(pattern)
    compiled_pattern.compile()

    assert compiled_pattern.is_compiled()

    uncompiled_pattern = pattern_registry.pattern_from_string(pattern)

    assert not uncompiled_pattern.is_compiled()

    pat1, pat2 = cycle_pickle((compiled_pattern, uncompiled_pattern), pickle_proto)

    assert pat1.is_compiled() is compiled_pattern.is_compiled()

    assert pat2.is_compiled() is uncompiled_pattern.is_compiled()


@pytest.mark.parametrize(
    ("pattern", "pickle_proto"),
    itertools.product(patterns, range(pickle.HIGHEST_PROTOCOL + 1)),
)
def test_properties(pattern: str, pickle_proto: int) -> None:
    pat = pattern_registry.pattern_from_string(pattern)
    pat.compile()

    inv_pat = pattern_registry.pattern_from_string("~" + pattern)
    inv_pat.compile()

    assert not pat.inverted
    assert inv_pat.inverted

    new_pat = cycle_pickle(pat, pickle_proto)
    new_inv_pat = cycle_pickle(inv_pat, pickle_proto)

    assert not new_pat.inverted
    assert new_inv_pat.inverted

    for _pat in cycle_pickle([pat], pickle_proto):
        assert not _pat.inverted

    for _pat in cycle_pickle(C(pat), pickle_proto).patterns:
        assert not _pat.inverted


@pytest.mark.parametrize(
    ("pattern", "pickle_proto"),
    itertools.product(patterns, range(pickle.HIGHEST_PROTOCOL + 1)),
)
def test_version_checks(pattern: str, pickle_proto: int) -> None:
    pat = pattern_registry.pattern_from_string(pattern)
    pat.compile()

    assert pat.is_compiled()

    data = pickle.dumps(pat, pickle_proto)

    # Change version
    v = polymatch.__version__.split(".")
    v[-1] = str(int(v[-1]) + 1)
    polymatch.__version__ = ".".join(v)

    new_pat = pickle.loads(data)

    assert new_pat.is_compiled()
