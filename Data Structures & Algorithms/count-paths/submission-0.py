class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1]*n for _ in range(m)]

        def dp(i,j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            
            cache[i][j] = (dp(i+1,j) + dp(i,j+1))

            return cache[i][j]

        return dp(0,0) 