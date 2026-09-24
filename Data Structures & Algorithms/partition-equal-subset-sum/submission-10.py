class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # total must be even. only need to find a subset that adds up
        # to half the total
        totalsum = sum(nums)
        if totalsum % 2 != 0:
            return False

        cache = {}
        def dfs(i,target):
            if (i,target) in cache:
                return cache[(i,target)]
            if target == 0:
                return True
            
            if target < 0 or i == len(nums):
                return False
            
            take = dfs(i+1,target-nums[i])
            skip = dfs(i+1,target)

            cache[(i,target)] = take or skip

            return cache[(i,target)] 

            
        return dfs(0,totalsum//2)
