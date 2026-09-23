class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        DIRECTIONS = [[0,1],[0,-1],[-1,0],[1,0]]

        steps = 0
        q = deque([])
        visited = {}

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))


        while q: 
            r,c = q.popleft()
            for dr,dc in DIRECTIONS:
                nr,nc = r+dr,c+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))

         

