class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # setup the hashmap
        # key is the number, value is the counts of frequency
        hashmap = {}
        # loop over the nums and counts the value
        for num in nums: 
            # if the current nums has appeared once before then value + 1
            hashmap[num] = 1 + hashmap.get(num, 0)

            # finally we can sort the value decreasely and return the key of the top k 
        return sorted(hashmap, key = hashmap.get, reverse = True)[:k]