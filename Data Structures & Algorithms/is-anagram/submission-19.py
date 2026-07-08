class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # the brute force solution is sorting the character of each string based on the alphbela but the time gona be onlogn and the space is o1
        # but the optimized solution could be using the hashmap because the key could be the alphbela and the value is the counting, if these two is matched, then we could return true otherwise false and the time gonna take on because of hashing but the space gonna be on because of using new data structure

        # edge case: if the two strings have different lengths, return false
        if len(s) != len(t): 
            return False

        # setup the new hashmap to store character frequencies for each string 
        countS = {}
        countT = {}
        
        # for loop both strings at the same time
        for i in range(len(t)): 
            # increase the character count for s[i] in the first map
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # increase the character count for t[i] in the second map
            countT[t[i]] = 1 + countT.get(t[i], 0)
            # after building both maps, compare them
        return countS == countT



