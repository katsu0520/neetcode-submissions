class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        last_index = {}
        l = 0
        for r in range(len(s)):
            if s[r] in last_index and last_index[s[r]]>=l:
                l = last_index[s[r]]+1
            last_index[s[r]] = r
            max_length=max(max_length,r-l+1)
        return max_length