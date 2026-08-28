class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = -1
        while l<r:
            m=(l+r)//2
            if nums[m]< nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m+1
        if l == r:
            m = l
        return nums[m]
        