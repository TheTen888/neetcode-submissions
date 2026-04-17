class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # compare the length first
        if len(s) != len(t):
            return False
        
        # create the dict 
        countS, countT = {}, {}

        # for loop: track the frequency of string 
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # for loop: compare the dict1 with dict2
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        return True



        
        