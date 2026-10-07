class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # to solve that, I want to use the hashmap for tracking the frequency. the key as the num and the value as the frequency then setup two hashmap for comparing each other then return True if same
        # edge case: length dismatch
        if len(s) != len(t):
            return False

        # init
        countS,countT = {}, {}

        # for loop 
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT