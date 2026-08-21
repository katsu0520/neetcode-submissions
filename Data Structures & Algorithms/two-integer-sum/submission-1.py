class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            component = target - nums[i]
            if component in seen:
                return [nums[component],i]
            seen[nums[i]] = i
