class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cursum = 0

        pref = {0:1}

        for num in nums:
            cursum += num
            diff = cursum - k
            res += pref.get(diff,0)

            pref[cursum] = 1 + pref.get(cursum,0)

        return res