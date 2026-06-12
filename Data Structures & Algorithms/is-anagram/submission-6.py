class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length of s not equal to the length of t, then return false 
        if len(s) != len(t):
            return False
        # setup two hashmap iterate each character and count, compare them 
        # key is character, value is the counts num
        countS, countT = {}, {}
        # loop over the indices， fill both maps at once
        for i in range(len(s)):
            # at each position I bump the count for each character
            # the get with a default of zero means I haven't seen the character before
            # start from zero and I add one 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # once both map are filled, go through every key in countS
        # and check if ti has the same count in countT
        # I use get with a default of zero again in case a character only shows up in s but isn't in t
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        # otherwise
        return True



