class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        max_count = 1
        for num in nums_set:
            count = 1
            if not num - 1 in nums_set:
                while num + 1 in nums_set:
                    count += 1
                    num = num + 1
            max_count = max(max_count,count)
        return max_count