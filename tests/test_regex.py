from polymatch import pattern_registry

data = (
    (r"regex::\btest\b", "test", True),
    (r"regex::\btest\b", "test1", False),
    (r"regex::\btest\b", "test response", True),
)


def test_patterns():
    for pattern, text, result in data:
        matcher = pattern_registry.pattern_from_string(pattern)
        matcher.compile()
        assert bool(matcher == text) is result
