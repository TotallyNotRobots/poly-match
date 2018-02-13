from polymatch import PolymorphicMatcher, pattern_registry


class ExactMatcher(PolymorphicMatcher):
    def compile_pattern(self, raw_pattern):
        return raw_pattern

    def compile_pattern_cs(self, raw_pattern):
        return raw_pattern

    def compile_pattern_ci(self, raw_pattern):
        return raw_pattern.lower()

    def compile_pattern_cf(self, raw_pattern):
        return raw_pattern.casefold()

    def match_text(self, pattern, text):
        return text == pattern


class ContainsMatcher(PolymorphicMatcher):
    def compile_pattern(self, raw_pattern):
        return raw_pattern

    def compile_pattern_cs(self, raw_pattern):
        return raw_pattern

    def compile_pattern_ci(self, raw_pattern):
        return raw_pattern.lower()

    def compile_pattern_cf(self, raw_pattern):
        return raw_pattern.casefold()

    def match_text(self, pattern, text):
        return text in pattern


pattern_registry.register('exact', ExactMatcher)
pattern_registry.register('contains', ContainsMatcher)
