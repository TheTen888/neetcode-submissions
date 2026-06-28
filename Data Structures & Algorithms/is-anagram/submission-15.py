class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap: key:character itself  value: frequency
        # edge case: if the length of two string are different, then return false
        if len(s) != len(t): 
            return False

        # initialize two hashmap
        countS, countT = {}, {}

        # loop over the character,  counting the value
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        # loop over the range(len(s)), compare the value if is valid anagram or not 
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True  