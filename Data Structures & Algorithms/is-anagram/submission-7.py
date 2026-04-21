class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort each string using sort() and compare
        return sorted(s) == sorted(t)