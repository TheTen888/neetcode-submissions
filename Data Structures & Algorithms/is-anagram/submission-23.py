class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # to solve this, my plan is to compare the character frequencies of both strings. I'll use a hashmap to track these counts. The time complexity is On since we iterate through the strings, and the space complexity is O1 because map will hold a max of 26 lowercase English letters
        # edge case: if the lengths not matched, we can return early
        # 1. edge case: len mismatch
        if len(s) != len(t):
            return False
        
        # 2.intializing a hashmap to track frequency 
        # 2. init maps 
        countS = {}
        countT = {}

        #for loop: now iterating through the array and count frequency
        # 3. build freq maps
        for i in range(len(s)):
            # 4increase the character count for s[i] in the first map
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # increase the character count for t[i] in the second map
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # 5. compare maps return True if they have the same frequency
        # 4. compare maps
        return countS == countT

        
            
            
        