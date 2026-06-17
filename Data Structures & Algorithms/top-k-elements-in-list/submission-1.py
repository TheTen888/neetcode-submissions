class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket list
        # hashmap: key: num; value: frequency
        # list: index: frequency(i); element: num(cnt)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # loop over the nums and count the num
        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        # loop over the count and transfer the num from the hashmap to the cnt in list 
        for num, cnt in count.items(): 
            freq[cnt].append(num)
        # initialize a empty list
        res = []
        # start from right to left（frequency)
        for i in range(len(freq) - 1, 0, -1):
            # loop over all num bucketed list
            for num in freq[i]:
                res.append(num)
                if len(res) == k: 
                    return res



