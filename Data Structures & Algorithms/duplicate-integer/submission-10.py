class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # setup the hashset
        # set naturally guarantees the unique elements 
        # hash enables O1 insertion and lookups
        # then the optimized solution is On time and On space
        seen = set()
        for num in nums: 
            if num in seen: 
                return True
            seen.add(num)
        return False 