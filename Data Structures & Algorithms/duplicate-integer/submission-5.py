class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # what kind of ds we should use? set why? because set can achieve o1 for looking up
        # what's the logic? if find the value appear in the set, then return True otherwise store in set until the end
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False