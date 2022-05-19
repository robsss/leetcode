class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = []
        for i in s:
            if i in subs:
                subs = []
            else:
                subs.append(i)
        return len(subs)
