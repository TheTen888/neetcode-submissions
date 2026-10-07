class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # to solve that, I will group the anagram by sorting each string alphabetically. Since any anagrams become identical once sorted, we can use the sorted string as the common hashkey to bucket these string values together. The time is (M * Nlogn) and the space is (M * N) 
        # Init:setup the empty list as the init value for first unique key
        res = defaultdict(list)
        # for loop
        for s in strs:
            # define the key as the sorted hashkey
            key = "".join(sorted(s))
            res[key].append(s)
        # return the list of the string values
        return list(res.values())
