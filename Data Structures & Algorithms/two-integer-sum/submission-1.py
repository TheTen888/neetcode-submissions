class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap {}
        premap = {}
        # for loop 
        for i, n in enumerate(nums):
            diff = target - n
            if diff in premap:
                return [premap[diff], i]
            premap[n] = i 
        return
