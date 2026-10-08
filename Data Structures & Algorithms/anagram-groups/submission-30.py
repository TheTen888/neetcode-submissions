class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I am going to group the anagrams by sorting alphatically and use the unique pattern to bucket these strings together. The data structure I am gonna use is hashmap. The time complexity is (M * Nlogn) since the sorting and the space complexity is On because we store the key and value in hashmap
        # init: setup the empty list as the value for first unique key 
        res = defaultdict(list)

        # for loop
        for s in strs: 
            # define the key and sorting it
            key = "".join(sorted(s))
            res[key].append(s)
        # return the list of the list
        return list(res.values()) 
        