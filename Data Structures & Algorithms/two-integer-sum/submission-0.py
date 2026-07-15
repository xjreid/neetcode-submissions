class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        n = len(nums)
        for i in range(n):
            if (target - nums[i]) in mydict:
                return [mydict[target-nums[i]], i];
            mydict[nums[i]] = i;
        return -1;