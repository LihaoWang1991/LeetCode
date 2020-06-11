# problem link: https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        stat_visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def dfs(r, c):
            stat_visited[r][c] = 1
            if grid[r][c] == "0":
                return
            for [i, j] in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0<=r+i<len(grid) and 0<=c+j<len(grid[0]) and stat_visited[r+i][c+j]==0:
                    dfs(r+i, c+j)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and stat_visited[r][c] == 0:
                    ans += 1
                    dfs(r, c)
        return ans