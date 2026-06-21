class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # setup the hashmap - key: diff, value: index
        prevMap = {}

        # for loop the nums and find the difference and return the index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i