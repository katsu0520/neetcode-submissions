import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = {}
        for num in nums:
            topK[num] = topK.get(num , 0) + 1
        h = heapq.nlargest(k,topK.keys(),key=topK.get)
        return h