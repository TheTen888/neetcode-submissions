class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # to solve that, the naive sorting approach takes onlogn, so instead I'll use the bucket sort based on frequency. Since any element's frequency is bounded between 1 and n, then we can use the frequency itself as an array index.Therefore we can return as much as k we want from right side. The time is on because counting frequencies and populating the buckets and scanning backwards each take linear time. The space is on to store the frequency and bucket list
        # init 
        count = {}

        # for loop
        for num in nums:
            # counting 
            count[num] = 1 + count.get(num, 0)
        # init buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        # populate buckets:
        for num, freq in count.items():
            buckets[freq].append(num)
        # for loop the res
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

                    

