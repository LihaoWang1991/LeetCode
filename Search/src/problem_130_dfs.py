# problem link: https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_r = len(board)
        num_c = len(board[0]) if num_r > 0 else 0
        visited = [[0 for _ in range(num_c)] for _ in range(num_r)]
        def dfs (r, c):   
            visited[r][c] = 1
            pos_list = [[r, c]]
            if r==0 or r==num_r-1 or c==0 or c==num_c-1: # O on the border
                contain_border_o = True
            else:
                contain_border_o = False
            for [i,j] in [[-1,0], [1,0], [0,-1], [0,1]]:
                next_r = r + i
                next_c = c + j
                if 0<=next_r<num_r and 0<=next_c<num_c and board[next_r][next_c]=="O" and visited[next_r][next_c]==0:
                    next_pos_list, next_contain_border_o = dfs(next_r, next_c)
                    pos_list += next_pos_list
                    contain_border_o = contain_border_o or next_contain_border_o
            return pos_list, contain_border_o
        
        def fill(pos_list):
            for [r, c] in pos_list:
                board[r][c] = "X"
                
        for r in range(num_r):
            for c in range(num_c):
                if board[r][c]=="O" and visited[r][c] == 0:
                    pos_list, contain_border_o = dfs(r, c)
                    if contain_border_o == False:
                        fill(pos_list)