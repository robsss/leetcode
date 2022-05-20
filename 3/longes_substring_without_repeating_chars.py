class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = []
        subs_longest = []
        for i in s:
            if i in subs:
                if len(subs) > len(subs_longest):
                    subs_longest = subs
                subs = []
                subs.append(i)
            else:
                subs.append(i)
        return len(subs_longest)
