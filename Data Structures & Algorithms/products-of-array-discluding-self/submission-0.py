class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [None] * n
        right = [None] * n
        left[0] = nums[0]
        right[n-1] = nums[n-1]
        for i in range(1, n):
            left[i] = left[i-1] * nums[i]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i]
        res = [None] * n
        for i in range(n):
            l = 1;
            if i - 1 >= 0:
                l = left[i-1]
            r = 1
            if i + 1 < n:
                r = right[i + 1]
            res[i] = l * r
        print(left)
        print(right)
        return res