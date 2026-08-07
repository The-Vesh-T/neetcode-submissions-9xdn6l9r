class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # a : 0,          b: 1
        dictonary = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for char in s:
                #freq = a: [0] b: [0] ..
                #becomes a: [1]
                freq[ord(char) - ord('a')] += 1
            dictonary[tuple(freq)].append(s)
        return list(dictonary.values())

