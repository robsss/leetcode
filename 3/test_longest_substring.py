from longes_substring_without_repeating_chars import Solution

class Test_Solution:
    def test_1():
        sln = Solution()
        assert sln.lengthOfLongestSubstring("abcabcbb") == 3
        assert sln.lengthOfLongestSubstring("bbbbb") == 1
        assert sln.lengthOfLongestSubstring("pwwkew") == 3
