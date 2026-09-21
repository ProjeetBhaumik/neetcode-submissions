class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i,remaining):
            if (i,remaining) in cache:
                return cache[(i,remaining)]
            if remaining == 0:
                return 0
            if remaining < 0 or i == len(coins):
                return float('inf')
            take = 1 + dfs(i,remaining - coins[i])
            skip = dfs(i+1,remaining)
            cache[(i,remaining)] = min(skip,take)
            
            return cache[(i,remaining)]
        
        ans = dfs(0,amount) 
        return -1 if ans == float('inf') else ans