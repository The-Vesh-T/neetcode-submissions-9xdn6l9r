class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force go over each num and add
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]