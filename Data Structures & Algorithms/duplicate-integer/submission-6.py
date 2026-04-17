class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Use a HashSet to for O(1) lookup
        known = set()
        #Iterate over elements since comparing that to set
        for i in nums:
            if i in known:
                return True
            known.add(i)
        return False