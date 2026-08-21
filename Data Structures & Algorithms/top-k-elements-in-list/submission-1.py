class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = {}
        for num in nums:
            topK[num] = topK.get(num , 0) + 1
        itmes = topK.items()
        sorted_items = sorted(itmes, key=lambda x:x[1], reverse= True)
        return [x[0] for x in sorted_items[:k]]
        