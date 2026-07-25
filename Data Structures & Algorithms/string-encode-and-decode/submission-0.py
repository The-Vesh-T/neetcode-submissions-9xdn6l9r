class Solution:

    def encode(self, strs: List[str]) -> str:
        #unique key to get length and differentiate the string
        result = ""
        for s in strs:
            result += str(len(s)) + "/" + s
        return result
    def decode(self, s: str) -> List[str]:
        #go through the string and get the length up until /
        result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '/':
                j += 1
            #everything from i to j is the number noti ncluding j
            length = int(s[i:j])
            #Append from infront of j to end length cause j is unikey
            result.append(s[j+1 : j+1+length])
            #iterate i once this all done or else infinite loop
            i = j + 1 + length
        return result
