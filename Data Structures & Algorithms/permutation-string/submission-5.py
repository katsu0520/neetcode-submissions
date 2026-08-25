class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1),len(s2)
        if n > m:
            return False
        target = {}
        for c in s1:
            target[c] = target.get(c,0) + 1
        
        count = {}
        l = 0
        for r in range(m):
            count[s2[r]] = count.get(s2[r],0)+1
            if r-l+1 > n:
                count[s2[l]]-=1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l+=1
            if count == target:
                return True
        return False