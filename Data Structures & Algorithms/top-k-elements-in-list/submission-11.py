class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num , 0) + 1
        buckets = []
        buckets = [[] for _ in range(len(nums)+1)]
        for num,freq in count.items():
            buckets[freq].append(num)
        output = []
        for i in range(len(buckets)-1, -1 , -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
