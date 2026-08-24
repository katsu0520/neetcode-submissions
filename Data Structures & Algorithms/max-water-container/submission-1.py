class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        area_max = min(heights[l],heights[r])*(r-l)
        while l < r:
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else:
                l+=1
                r-=1
            area = min(heights[l],heights[r])*(r-l) 
            area_max = max(area_max,area)
        return area_max
            
        