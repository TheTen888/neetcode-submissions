class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force is counting the frequency first then sorting the frequency and return the top k
        # the optimal solution here is use a bucket list by leveraging the array index are inherently ordered cuz the index running from 0 to the length of the array right, we can loop the list inversely then return the top k frequency value
        # initialize the data structure hashmap for counting frequency and nested list as two-dimensional structure where each index as the freqency and the value is the num
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # run a loop over nums to aggregate the counts
        for num in nums: 
            count[num] = count.get(num, 0) + 1
        
        # run a loop over the hashmap to move the num to the value of the list
        for num, cnt in count.items():
            freq[cnt].append(num)\
        
        # initialize a empty list res to save the top k most frequency num and return it
        res = []

        # loop through the bucket backward from len(freq) -1 down to 0
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res