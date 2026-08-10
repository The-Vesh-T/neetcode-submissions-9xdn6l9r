class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use a set all that matters is making sure none before it
        seen = set(nums)
        longest = 0

        for num in seen:
            if(num-1) not in seen:
                length = 1
                while (num+length) in seen:
                    length +=1
                longest = max(longest, length)
        return longest