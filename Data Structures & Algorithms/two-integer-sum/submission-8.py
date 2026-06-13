class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the question is asking about find the sum of the elemnts equal to the target, if find it, return their index otherwise return nothing
        # we can use hashmap here the key is the diff and the value is the index of that diff number 
        # this optimized solution perform O1 lookup time cost and On space cost
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
        return