"""
Tset for longest palindromic substring
"""
from longest_palindromic_substring import Solution


class TestSolution:
    """test"""
    def test_1(self):
        sln = Solution()
        s = "babad"
        assert sln.longest_palindrome(s) in ["bab", "aba"]

    def test_2(self):
        sln = Solution()
        s = "cbbd"
        assert sln.longest_palindrome(s) == "bb"

