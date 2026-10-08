class Solution:
    # To solev that, I am gonna use the encoding format "length#string" and decode the string to list.Time is O(n) for both encode and decode where n is the total number of characters across all strings. Space is O(m + n) where n is the number of string
    def encode(self, strs: List[str]) -> str:
        # init res as string space
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # init res as list & i as index
        res, i = [], 0

        # while loop for tracking
        # calculate the length 
        while i < len(s):
            j = i 
            while s[j] != '#': 
                j += 1
            length = int(s[i:j])
            # append the string to res
            res.append(s[j + 1: j + 1 + length])
            # update i 
            i = j + 1 + length
        return res
            
        
