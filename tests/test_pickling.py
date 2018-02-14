import pickle


def test_compile_state():
    from polymatch import pattern_registry
    compiled_pattern = pattern_registry.pattern_from_string("regex::test")
    compiled_pattern.compile()

    assert compiled_pattern.is_compiled()

    uncompiled_pattern = pattern_registry.pattern_from_string("regex::test")

    assert not uncompiled_pattern.is_compiled()

    data = pickle.dumps((compiled_pattern, uncompiled_pattern))

    pat1, pat2 = pickle.loads(data)

    assert pat1.is_compiled() is compiled_pattern.is_compiled()

    assert pat2.is_compiled() is uncompiled_pattern.is_compiled()
