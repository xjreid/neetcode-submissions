class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        n = len(nums);
        for i in range(n):
            if nums[i] in num_set: 
                return True;
            num_set.add(nums[i])
        return False;