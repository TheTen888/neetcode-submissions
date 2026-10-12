class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # to solve that, I will use the bucket sort based on the frequency. Since any element's frequency is bounded between 1 and N. then we can use the frequency as the array index. Then we can return the list based on the k. The time complexity is On since counting frequency and populating the buckets and scanning backwards each take linear time and the space complexity is On to store the frequency and bucket list
        # init count
        count = {}

        # for loop: value as counting
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # init the empty bucket list
        buckets = [[] for _ in range(len(nums) + 1)]
        # populating bucket
        for num, freq in count.items():
            buckets[freq].append(num)
        # init scanning backwards
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k: 
                    return res

        
        