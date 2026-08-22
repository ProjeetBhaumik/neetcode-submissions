class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = {0:1}
        total = 0
        res = 0
        for num in nums:
            total += num
            diff = total - k

            res += pref.get(diff,0)
            pref[total] = pref.get(total,0) + 1

        return res