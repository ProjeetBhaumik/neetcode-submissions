class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
    
    def helper(self,nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0]*n
        for i in range(n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[n-1]