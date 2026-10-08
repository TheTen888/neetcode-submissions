class Solution:
    # asking about how do we encode the list and decode as the original list 
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # setup the res list and i 
        res, i = [], 0
        # while loop for str
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res



