class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # to solve that, I'll group the anagram by sorting each string alphabetically, since any anagrams become identical once sorted. then we can use the sorted string as the common hashkey to bucket these string values together. the time is Onlogn since sorting and the space is On to store the number of string
        # init: set up the empty list for the first pattern
        res = defaultdict(list)

        # for loop: track the 
        for s in strs:
            key = "".join(sorted(s))
            res[key].append(s)
        return list(res.values())
        