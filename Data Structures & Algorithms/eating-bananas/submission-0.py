import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (l+r)//2
            eating_hours = 0
            for i in range(len(piles)):
                eating_hours += math.ceil(piles[i]/m)
            if eating_hours <= h:
                res = m
                r = m-1
            elif eating_hours > h:
                l = m+1
        return res
        