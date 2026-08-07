class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before = n * [0]
        after = n * [0]
        result = n*[0]
        before[0] = after[n-1] = 1

        for i in range(1, n):
            before[i] = before[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            after[i] = after[i+1] * nums[i+1]
        for i in range(n):
            result[i] = before[i] * after[i]
        return result