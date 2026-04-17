class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ds: for achieving o1 lookup choose hashmap
        # 1. sorting
        hashmap = {}

        for s in strs:
            # define key as the sorted value
            key = tuple(sorted(s))
            # if key not in the hashmap we can initialize a new empty list
            if key not in hashmap:
                hashmap[key] = []
            # add the s to the specific key 
            hashmap[key].append(s)
        # return all the value at the hashmap
        return list(hashmap.values())