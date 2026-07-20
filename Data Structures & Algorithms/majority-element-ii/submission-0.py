class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        size = int(n/3)
        res = []
        for key in freq.keys():
            if freq[key] > size:
                res.append(key)
        return res