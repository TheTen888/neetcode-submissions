class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap: key: difference, value is index of that diff num
        hashmap = {}

        # for loop the nums
        for i, num in enumerate(nums): 
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
        return 
            