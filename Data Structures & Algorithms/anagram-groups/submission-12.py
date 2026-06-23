class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # bucket list? 
        # setup the hashmap, key: counting/ value: bucket list
        res = defaultdict(list)

        for s in strs:
            # initialize empty list
            count = [0] * 26
        # for loop the s and counting 
            for char in s:
                count[ord(char) - ord('a')] += 1

            # convert the list to the tuple because key must be immutale 
            key = tuple(count)

            # append the value to the hashmap
            res[key].append(s)
        return list(res.values( ))
    

        
