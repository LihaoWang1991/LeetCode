# problem link: https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        num_row = len(grid)
        num_col = len(grid[0])
        stat_visited = [[0 for i in range(num_col)] for _ in range(num_row)]
        def dfs(row, col):
            cur_area = 1
            stat_visited[row][col] = 1
            if grid[row][col] == 0:
                return 0
            else:
                for [i,j] in [[-1,0],[1,0],[0,-1],[0,1]]:
                    if 0 <= row+i < num_row and 0 <= col+j < num_col and stat_visited[row+i][col+j] == 0:
                        cur_area += dfs(row+i, col+j)
            return cur_area
        
        for row in range(num_row):
            for col in range(num_col):
                if grid[row][col] == 1 and stat_visited[row][col] == 0:
                    res = max(res, dfs(row, col))
        return res