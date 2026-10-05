class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i am gonna find the diff which is the target - nums, the diff will be stored in the hashmap and the key is num and the value is index, if we meet the diff in the hashmap then return it index and current num index. The time complexity is On since the nums.length and number range are so large and the space complexity is On cuz we gonna use hashmap for storing num
        # init hashmap
        hashmap = {}

        # for loop 
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        return 