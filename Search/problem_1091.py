# problem link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        if grid == [[0]]:
            return 1
        stat_visited = [[0 for _ in range(N)] for _ in range(N)]  # mark if some point is already visited
        queue = [[0,0,1]]   # [x, y, path length up to now]
        while queue != []:
            [cur_r, cur_c, cur_len] = queue.pop(0)
            for [delta_r, delta_c] in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                next_r, next_c = cur_r + delta_r, cur_c + delta_c
                if 0<=next_r<N and 0<=next_c<N and grid[next_r][next_c]==0 and stat_visited[next_r][next_c]==0:
                    if next_r == next_c == N-1:    # reach the terminal
                        return cur_len + 1
                    queue.append([next_r, next_c, cur_len + 1])
                    stat_visited[next_r][next_c] = 1
        return -1