class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP,minP = 1, 1
        res = nums[0]
        for num in (nums):
            tmp = maxP * num
            maxP = max(maxP*num,minP*num,num)
            minP = min(tmp,minP*num,num)
            res = max(maxP,res)
        return res
            