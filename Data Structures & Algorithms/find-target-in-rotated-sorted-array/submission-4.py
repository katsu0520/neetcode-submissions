class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l=m+1
                else:
                    r=m
            else:
                if nums[l]<= target <=nums[m]:
                    r=m
                else:
                    l=m+1
        if target == nums[l]:
            return l
        else:
            return -1