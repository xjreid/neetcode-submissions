class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1, n):
            ind = i
            while nums[ind] < nums[ind-1] and ind > 0:
                self.swap(ind, ind-1, nums)
                ind -= 1
    def swap(self, ind1, ind2, nums: List[int]) -> None:
        n1 = nums[ind1]
        n2 = nums[ind2]
        nums.pop(ind1)
        nums.insert(ind1, n2)
        nums.pop(ind2)
        nums.insert(ind2, n1)

        