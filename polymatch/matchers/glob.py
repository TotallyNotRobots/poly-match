from fnmatch import translate

from polymatch.base import CaseAction
from polymatch.matchers.regex import RegexMatcher


class GlobMatcher(RegexMatcher):
    def __init__(self, pattern, case_action=CaseAction.NONE, invert=False):
        if isinstance(pattern, bytes):
            # Mimic how fnmatch handles bytes patterns
            pat_str = str(pattern, 'ISO-8859-1')
            res_str = translate(pat_str)
            res = bytes(res_str, 'ISO-8859-1')
        else:
            res = translate(pattern)

        super().__init__(res, case_action, invert)
