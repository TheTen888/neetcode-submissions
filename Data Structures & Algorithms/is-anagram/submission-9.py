class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # question is asking about if the two string has same character even the order is different 
        # if has the exact same character, return True, otherwise false
        # I will go for hashmap the key gonna track the character and the value gonna track the counts
        # first edge case is comparing the length if not return False immediately
        # then we use the hashmap to lookups the two string and counts each character if appear once
        # finally lookups the whole map and compare with the string S

        # setup hashmap
        countS, countT = {}, {}
        # edge case: if length is different return false
        if len(s) != len(t): 
            return False
        # loop over the two string and add to hashmap
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # loop over the hashmap and compare with S
        for n in countS:
            if countS[n] != countT.get(n,0):
                return False
        return True 



        