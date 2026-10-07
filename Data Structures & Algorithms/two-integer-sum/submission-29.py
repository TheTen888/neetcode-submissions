class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # to solve that, I am gonna use the hashmap for tracking the num and its index. the key is num and the value is its index. the time complexity is On because 2 <= nums.length <= 100 and the space complexity is On since we use the hashmap for tracking
        # init 
        hashmap = {}

        # for loop
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
        return 