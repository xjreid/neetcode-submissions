class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(nums)
        for num in freq.keys():
            if freq[num] > n/2:
                return num
        
        return -1