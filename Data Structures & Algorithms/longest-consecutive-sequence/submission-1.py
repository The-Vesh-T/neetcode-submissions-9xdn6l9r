class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        result = 0

        for num in nums:
            length = 0
            if num-1 not in seen:
                length= 1
                while num+1 in seen:
                    length+=1
                    num+=1

                result = max(length, result)
        return result
