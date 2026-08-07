class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Iterate the string add each letter to freq map
        S = {}
        T = {}
        if len(s) != len(t):
            return False

        #iterate through each oh amke sure same length
        for i in range(len(s)):
            S[s[i]] = 1 + S.get(s[i], 0)
            T[t[i]] = 1 + T.get(t[i], 0)
        return S == T