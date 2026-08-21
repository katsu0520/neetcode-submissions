class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))
        max_count = 1
        count = 1
        for i in range(len(sorted_nums)):
            if i+1 < len(sorted_nums) and 1 == sorted_nums[i+1]-sorted_nums[i]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        return max_count