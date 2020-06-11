# problem link: https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        num_r = len(matrix)
        num_c = len(matrix[0]) if num_r > 0 else 0
        can_reach_p = [[False for _ in range(num_c)] for _ in range(num_r)]   # mark if one point can reach pacific ocean
        can_reach_a = [[False for _ in range(num_c)] for _ in range(num_r)]   # mark if one point can reach atlantic ocean
        def dfs(r, c, p_or_a):
            can_reach = can_reach_p if p_or_a == "p" else can_reach_a
            if can_reach[r][c] == True:
                return
            can_reach[r][c] = True
            for [i,j] in dirs:
                next_r = r + i
                next_c = c + j
                if 0<=next_r<num_r and 0<=next_c<num_c and matrix[r][c]<=matrix[next_r][next_c]:
                    dfs(next_r, next_c, p_or_a)
                    
        for r in range(num_r):
            dfs(r, 0, "p")
            dfs(r, num_c - 1, "a")
        for c in range(num_c):
            dfs(0, c, "p")
            dfs(num_r - 1, c, "a")              
        for r in range(num_r):
            for c in range(num_c):
                if can_reach_p[r][c] and can_reach_a[r][c]:
                    ans.append([r,c])
        return ans