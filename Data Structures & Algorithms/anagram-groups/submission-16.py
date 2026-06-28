class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap: key: counting frequency by alphbelt value: bucketlist for same str
        # if the length and the character frequency is same, then store it in the same bucket
        res = defaultdict(list)

        # loop over the strs, set up the empty initial frequency of the array
        for s in strs: 
            count = [0] * 26

        # count the frequency, turn the alphabet as the counts for each string
            for c in s:
                count[ord(c) - ord('a')] += 1

        # append the values to the hashmap and match with the key
            res[tuple(count)].append(s)
        return list(res.values())
