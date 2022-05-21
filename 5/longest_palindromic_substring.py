"""
5. Longest Palindromic Substring

What is the meaning palindromic?
reads the same backward or forward
: a word, phrase, sentence, or number that reads the same backward or forward
  "Step on no pets"

Given a string s, return the longest palindromic substring in s.

 Example 1:

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

Example 2:

```
Input: s = "cbbd"
Output: "bb"
 ```

Constraints:

- 1 <= s.length <= 1000
- s consist of only digits and English letters.

"""

class Solution:
    def longest_palindrome(self, s: str) -> str:
        # first find the palindromes
        # then compare them
        palindromes = self.palindrs(s)
        longest = self.longest_palindr(palindromes)
        return longest


    def palindrs(self, s: str) -> list[str]:
        """
        Find all possible palindrome

        input: s
        return: all palindromes
        """
        palindromes = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                print(i)
                sub = s[i:j]
                if self.is_palindr(sub):
                    palindromes.append(sub)
        return palindromes


    def is_palindr(self, s: str) -> bool:
        """ditinguish palindromic string"""
        if s == s[::-1]:
            return True
        else:
            return False


    def longest_palindr(self, pals: list[str]) -> str :
        """find the longest palindrome"""
        longest = pals[0]
        for s in pals:
            if len(s) > len(longest):
                longest = s
        return longest


def main():
    sln = Solution()
    s = "babad"
    r = sln.longest_palindrome(s)
    print(r)


if __name__ == "__main__":
    main()

