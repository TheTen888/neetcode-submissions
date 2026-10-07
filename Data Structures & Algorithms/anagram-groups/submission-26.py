class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # to solve this, I'll group anagrams by sorting each string alphabetically. Since any anagrams become identical once sorted like tea, eat, aet all as the aet, we can use the sorted string as the common hashkey to bucket the value together. The time complexit is (O m * nlogn) because we sort each of the m strings of length n and the space complexity is O(m * n) to store all strings and keys inside the hashmap
        # init: setup the empty list as the init value for unique key
        res = defaultdict(list)

        # for loop
        for s in strs:
            # join the sorted value together
            key = "".join(sorted(s))
            res[key].append(s)
        return list(res.values())