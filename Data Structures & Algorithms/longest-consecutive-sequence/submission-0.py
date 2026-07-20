class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        check = set()
        for n in nums:
            check.add(n)
        res = 1
        for key in check:
            count = 1
            curr = key
            while key + 1 in check:
                count += 1
                key += 1
            res = max(res, count)
        return res
        