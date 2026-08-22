class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j):
            if i < 0 or i >= rows \
            or cols <= j or j < 0 or grid[i][j] != "1":
                return
            else:
                grid[i][j] = "0"
                dfs(i,j-1)
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i-1,j)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
        return count
