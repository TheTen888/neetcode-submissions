class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # setup the two hashmap: key is the string, value is the counting
        countS, countT ={}, {}
        v = 0
        # edge case
        if len(s) != len(t):
            return False
        
        # loop over the s & t and counting
        for i, v in enumerate(s):
            countS[v] = countS.get(v, 0) + 1 
            countT[t[i]] = countT.get(t[i], 0) + 1

        # loop over and compare the V
        for v in countS:
            if countS[v] != countT.get(v, 0):
                return False
        return True 