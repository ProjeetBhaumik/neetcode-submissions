class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 1:
            return 0
        
        if n < 2:
            return 1
            
        dp = [-1]*(n+1)
        dp[0] = 0
        dp[1] = dp[2] = 1

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            dp[i]= dfs(i-1)+ dfs(i-2) + dfs(i-3)
            return dp[i]
        
        return dfs(n)
