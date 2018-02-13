from polymatch import pattern_registry

data = (
    ("glob::*", "", True),
    ("glob::*?", "", False),
    ("glob::*?", "a", True),
)


def test_patterns():
    for pattern, text, result in data:
        matcher = pattern_registry.pattern_from_string(pattern)
        matcher.compile()
        assert bool(matcher == text) is result
