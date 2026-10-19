class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the brute force is treat every element as the start of the sequence and counting the longest consecutve sequence. But the optimized way is tracking the start of the sequence until no left neighbor and counting the length until find the max one. 
        # init: create the set for tracking the start of sequence
        numsSet = set(nums)
        longest = 0 

        # for loop: iterative through the num in nums 
        for n in nums: 
            if (n - 1) not in numsSet: 
                length = 0 
                while(n + length) in numsSet: 
                    length += 1
                    longest = max(longest, length)
        return longest 