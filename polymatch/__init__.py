# SPDX-FileCopyrightText: 2018-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

"""Polymorphic pattern matchers."""

from polymatch._version import (
    __version__,
    __version_tuple__,
    version,
    version_tuple,
)
from polymatch.base import CaseAction, PolymorphicMatcher
from polymatch.error import (
    DuplicateMatcherRegistrationError,
    NoMatchersAvailableError,
    NoSuchMatcherError,
    PatternCompileError,
    PatternNotCompiledError,
    PatternTextTypeMismatchError,
)
from polymatch.registry import pattern_registry

__all__ = [
    "CaseAction",
    "DuplicateMatcherRegistrationError",
    "NoMatchersAvailableError",
    "NoSuchMatcherError",
    "PatternCompileError",
    "PatternNotCompiledError",
    "PatternTextTypeMismatchError",
    "PolymorphicMatcher",
    "__version__",
    "__version_tuple__",
    "pattern_registry",
    "version",
    "version_tuple",
]
