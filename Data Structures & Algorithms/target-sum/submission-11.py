class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i,remaining):
            if i == len(nums):
                return remaining == 0

            if (i,remaining) in cache:
                return cache[(i,remaining)]
            
            add = dfs(i+1,remaining-nums[i])
            sub = dfs(i+1,remaining+nums[i])

            cache[(i,remaining)] = add + sub
            return cache[(i,remaining)]

        return dfs(0,target)