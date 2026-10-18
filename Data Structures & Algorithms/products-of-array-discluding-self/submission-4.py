class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force is every num product of all element of nums except itself so the time cost On^2 and space cost On. The optimized way is simply the product of everything to its left multiplied by everything to its right. we can compute this in On time and O1 space by first storing the prefix products directly into the output array and then multiplying them by running postfix product in a reverse pass
        # init: initialize the array 
        res = [1] * len(nums)

        # calculate the prefix
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # calculate the postfix 
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): 
            res[i] *= postfix
            postfix *= nums[i]
        return res