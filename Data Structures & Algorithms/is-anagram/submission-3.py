class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Use a hash table with counter.
        countS, countT = {}, {}
        for i in range(len(s)):
            #letter : count
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
