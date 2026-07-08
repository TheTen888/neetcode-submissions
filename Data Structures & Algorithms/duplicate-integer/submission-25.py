class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # this is question is asking if the array has the duplicate value then return true
        # if not return false
        # i am gonna choose the data structure as set because naturally set can only contain the unique value, if has the duplicate value then it gonna return false

        # setup the initial empty set called hashset
        hashset = set()

        # for loop the entire array nums
        for num in nums: 
            if num in hashset:
                return True
            hashset.add(num)
        return False


        