class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        # loop over the nums
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False