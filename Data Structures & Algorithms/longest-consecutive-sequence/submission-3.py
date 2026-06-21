class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hashmap we can use key to find the value(what's the res we wanna return)
        # first solution is sorting but On^2 
        # setup another array to store the value if we found the n+1 num until the range(len(nums))
        # or can we still use the solution with bucket list? 
        # 我的想法是我们每次loop到任意num都去找它的+1项，可以先存一下+1项，如果找到了+1项那我们就存入到value里？然后直到最后loop完所有的num我们再sort出最长的consecutive sequence of elements ？
        # 把 nums 丢进一个 set（O(1) 查找）。
        # longest = 0。
        # 遍历 set 里每个数 n：
        #如果 n-1 不在 set 里（说明 n 是某段的起点）：从 1 开始数，只要 n+1、n+2…… 还在 set 里就继续加，得到这段长度。
        # longest = max(longest, 这段长度)。
        # 返回 longest。
        hashset = set(nums)
        longest = 0 
        for num in nums: 
            if (num - 1) not in hashset:
                current_num = num
                current_length = 1
                while (current_num + 1) in hashset: 
                    current_num += 1
                    current_length += 1
                longest = max(longest, current_length)
        return longest 