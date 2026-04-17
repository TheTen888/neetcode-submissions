class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create the set because we wanna return true if we found the same element
        # why use set here instead of other data structure? 
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False