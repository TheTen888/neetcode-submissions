class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # setup the hashset
        # set naturally guarantees the unique elements 
        # hash enables O1 insertion and lookups
        # then the optimized solution is On time and On space
        hashset = set()
        # loop over the array 
        for num in nums: 
            # if we've seen the same number before, return True
            if num in hashset: 
                return True
            # if not, add the num in the set 
            hashset.add(num)
        return False 