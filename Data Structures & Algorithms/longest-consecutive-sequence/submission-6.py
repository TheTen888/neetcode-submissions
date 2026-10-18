class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the brute force is treat every element as the start of sequence then iteratively check n + 1,+ 2 exist in the array, and counting if there is a consecutive sequence whcih take On^2 time and On space. The optimized way is convert the array to the set for tracking the start of the sequence then counting the length of the consecutive sequence. The time cost On and space cost On
        # init: we need to create the set for the inital array nums
        numSet = set(nums)
        # track the longest consecutive sequence intially we can say it 0 
        longest = 0 

        # we iterate through every number in the nums
        for num in nums: 
            if (num - 1) not in numSet: 
                length = 0 
                while (num + length) in numSet: 
                    length += 1 
                    longest = max(length, longest)
        return longest 
        