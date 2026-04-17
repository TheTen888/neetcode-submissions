class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # big o = o1 retrieve : hashmap
        # if find the diff, return index of target and n 
        # WHAT SHOULD RETURN? : if find the target return index of target and n if not store n 
        prevmap = {}

        for i, n in enumerate(nums): 
            diff = target - n
            if diff in prevmap: 
                return [prevmap[diff], i]
            prevmap[n] = i 
        return 