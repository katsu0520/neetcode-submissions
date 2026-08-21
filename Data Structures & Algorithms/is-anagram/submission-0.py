class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for i in range(len(s)):
            seen[s[i]] = i
        for i in range(len(t)):
            if not t[i] in seen:
                return False
        return True 
            