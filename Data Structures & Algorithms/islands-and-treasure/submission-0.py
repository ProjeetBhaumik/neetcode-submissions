class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647
        directions = [(0,1),(0,-1),(-1,0),(1,0)]

        def bfs(r,c):
            visited = set()
            q = deque([(r,c)])
            steps = 0
            while q:
                for _ in range(len(q)):
                    row,col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr,dc in directions:
                        nr,nc = row+dr,col+dc
                        if (0 <= nr < rows and \
                        0 <= nc < cols and \
                        (nr,nc) not in visited and \
                        grid[nr][nc] != -1):
                            
                            visited.add((nr,nc))
                            q.append((nr,nc))
                steps += 1
                    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)
