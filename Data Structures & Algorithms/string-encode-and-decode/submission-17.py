class Solution:
    # to solve that, i am gonna use the encoding format "length#string" and decode the string to the list, and for the decode part, I am gonna use the two pointer to get the length number and get the string from the list. The time is On for both encode and decode where n is the total number of character accross all string. The space is On where n is the number of string
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        # init res as list and i as index
        res, i = [], 0
        
        # for loop：slice string to list
        while i < len(s):
            j = i
            while s[j] != "#": 
                j+= 1
            length = int(s[i:j])
            # append the string to res
            res.append(s[j + 1:j + 1 + length]) 
            # update the i
            i = j + 1 + length 
        return res
