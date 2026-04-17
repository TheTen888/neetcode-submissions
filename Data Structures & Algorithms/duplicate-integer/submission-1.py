class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create the set 
        hashset = set()
        # for loop and loop in set if set already has this value return false otherwise return true
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


        