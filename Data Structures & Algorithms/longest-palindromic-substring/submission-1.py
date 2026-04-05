class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.resLen = 0

        for i, _ in enumerate(s):
            self.helper(s, i, i)

            self.helper(s, i, i+1)

        return self.res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > self.resLen:
                self.res = s[l:r+1]
                self.resLen = r - l + 1
            l -= 1
            r += 1
        