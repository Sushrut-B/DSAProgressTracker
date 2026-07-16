class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        res = ""
        reslen = 0

        for i in range(n):
            # Odd length palindrome
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > reslen:
                    res = s[left:right+1]
                    reslen = right - left + 1
                left -= 1
                right += 1

            # Even length palindrome
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > reslen:
                    res = s[left:right+1]
                    reslen = right - left + 1
                left -= 1
                right += 1

        return res
        