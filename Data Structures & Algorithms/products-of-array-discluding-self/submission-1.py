class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before = [1] * n
        after = [1] * n
        res = [0] * n
        # Prefix products
        for i in range(1, n):
            before[i] = before[i - 1] * nums[i - 1]
        # Suffix products
        for i in range(n - 2, -1, -1):
            after[i] = after[i + 1] * nums[i + 1]
        # Result
        for i in range(n):
            res[i] = before[i] * after[i]
        return res