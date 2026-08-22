class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxS = nums[0]
        currS = 0
        for num in nums:
            if currS<0:
                currS = 0
            currS += num
            maxS = max(currS,maxS)
        return maxS