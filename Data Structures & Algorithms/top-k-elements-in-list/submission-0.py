class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        maxHeap = []
        for key in freq.keys():
            heapq.heappush(maxHeap, (-freq[key], key))
        res = []
        while k > 0:
            res.append(heapq.heappop(maxHeap)[1])
            k -= 1
        return res