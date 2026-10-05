class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # to solve that, I can use the hashmap for tracking num if i found the diff num before then return it. The time complexity is On since length almost 1000 and -10,000,000 <= nums[i] <= 10,000,000 and space complexity is On because we will use the hashmap for tracking

        # 2. init hashmap： key: difference, value is index of that diff num
        hashmap = {}


        # 3. for loop
        for i,num in enumerate (nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
        return 
