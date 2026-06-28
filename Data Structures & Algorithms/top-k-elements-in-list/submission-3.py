class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap; key: number value: counting frequency
        # bucket list(index as the frequency, value as the num)
        # list: index: frequency(i); element: num(cnt)
        hashmap = {}
        list = [[] for i in range(len(nums) + 1)]

        # loop over the nums and count the num in hashmap
        for num in nums: 
            # fill the num and counting in the empty hashmap
            hashmap[num] = hashmap.get(num, 0) + 1
        
        # loop pver hashmap and transfer the num to list[cnt]
        for num, cnt in hashmap.items():
            list[cnt].append(num)

        # initialize an empty list to save the top k num
        res = []

        # start from right to left(frequency)
        for i in range(len(list) - 1, 0, -1):
            # loop over all num bucket list
            for num in list[i]:
                res.append(num)
                if len(res) == k:
                    return res
