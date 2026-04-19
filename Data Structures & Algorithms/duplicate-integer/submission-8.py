class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #If the set is shorter than list, a dupe must be in list
        #Set auto removes dupes!
        return len(set(nums)) < len(nums)