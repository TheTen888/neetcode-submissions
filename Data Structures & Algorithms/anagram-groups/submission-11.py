class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # setup the hashmap to return the value finally
        # setup the tuple as the key which is the counts by alphbelt
        # value is the group of string that has same character  
        # finally return the value
        # edge case: if key is not exist, it will setup the empty list 
        res = defaultdict(list)

        # loop over the strs, setup the initial frequency of the array
        for s in strs: 
            count = [0] * 26
            # count the frequency, turn the alphabet as the counts for each string
            for c in s: 
                count[ord(c) - ord('a')] += 1
            # append the values to the hashmap and match with the key
            res[tuple(count)].append(s)
        return list(res.values())           
            

        