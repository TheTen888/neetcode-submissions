class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # so the brute force is treat every element as the start of a sequence then iteratively check if num + 1 or + 2 exist in the array. and counting if there is a consecutive sequence which take On^2 on time and On space. The optimized way is we could conver the array to set for tracking the start of the sequence then counting the length of the consecutive sequence. the time cost gonna be O(n) and space is O(n). 
        # we need to create a set from the initial array nums
        numset = set(nums)
        # track the longest consecutive sequence is initially we can say it's 0 
        longest = 0 
        # for loop: we want to iterate through every number in nums
        for n in nums: 
            # we want to check if it's the start of the sequence, we can simply by checking if n - 1 does not exist in the numset if this number does not have the left neighbor that means start of sequence. 
            if (n - 1) not in numset: 
                # now we want to ge the length of the sequence iunitially we can say the length is 0 and we want to keep getting each consecutive number and checking if it exist in our num set if exist then expanding the length
                length = 0 
                # so initially i'm going to check n + length because that's going to check the current number as the length grows we could have potentially found the longest sequence 
                while (n + length) in numset: 
                    length += 1 
                longest = max(length,longest)
        return longest 


