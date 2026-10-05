class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # i am gonna use the set for comparing, if has duplicate value then return true. Time complexity is On since the large range number and the space complexity is On because we will use set for storing
        # edge case: empty nums
        if len(nums) == 0: 
            return False
        
        # init set
        hashset = set()

        # for loop
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False