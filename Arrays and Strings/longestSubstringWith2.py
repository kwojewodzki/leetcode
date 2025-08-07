'''Given a string s, return the length of the longest substring that contains at most two distinct characters.'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = r = 0
        uniqueChars = {}
        max_len = 2
        while r < len(s):
            uniqueChars[s[r]] = r
            r += 1

            if len(uniqueChars) == 3:
                del_idx = min(uniqueChars.values())
                del uniqueChars[s[del_idx]]
                l = del_idx + 1
                max_len = max(max_len, r - l)
        return max_len
        print(uniqueChars)


s = "ccaabbb"

sol = Solution()
print(sol.lengthOfLongestSubstringTwoDistinct(s))