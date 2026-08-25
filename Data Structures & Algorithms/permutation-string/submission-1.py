class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length=len(s1)
        s2_length=len(s2)
        i = 0
        target = sorted(s1)
        while i + s1_length <= s2_length:
            if target == sorted(s2[i:i+s1_length]):
                return True
            i+=1
        return False
        