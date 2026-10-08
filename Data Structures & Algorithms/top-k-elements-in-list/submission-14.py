class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # to solve that, I wil use the bucket sort based on frequency. Since any element's frequency is bounded between 1 and n, then we can use the frequency itself as the array index. Then we can return as much as k we want. The time complexity is On because counting frequency and populating the buckets and scanning backwards each take linear time and the space complexity is On to store the frequency and bucket list
        # init count
        count = {}

        # for loop: value as counting
        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        # init bucket 
        buckets = [[] for _ in range(len(nums) + 1)]
        # populating buckets
        for num, freq in count.items():
            buckets[freq].append(num)
        # init res for scanning backwards
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

            




            
            
        
            