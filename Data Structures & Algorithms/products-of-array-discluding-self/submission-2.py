class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we need the prefix(left to right) to store the pre multiplication in res
        # need the postfix(right to left) to multiple with the prefix to update the res
        # initialize res array 
        res = [1] * len(nums)

        # prefix
        prefix = 1
        for i in range(len(nums)): 
            res[i] = prefix
            prefix *= nums[i]

        # postfix
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i]
    
        return res