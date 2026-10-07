class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # to solve that, I want to use set for check whether have the duplicate value if we've met before then return True. Because set naturally can not hold duplicate values. Then the time complexity is On since 0 <= nums.length <= 10^5 and the space complexity is On because we use set for comparing
        # init 
        hashset = set()

        # for loop
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False