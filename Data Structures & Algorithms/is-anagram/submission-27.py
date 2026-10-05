class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # I gonna use the hashmap for tracking frequency. the reason why I choose hashmap because it could track the num as key and frequency as value, then return true if same frequency. The time complexity is O1 because s and t consist of only 26 lowercase English letters and the space complexity is On since we gonna use the hashmap for storing
        # edge case: check match
        if len(s) != len(t):
            return False
        
        # init: two hashmaps for tracking frequency
        countS,countT = {}, {}

        # for loop 
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT   