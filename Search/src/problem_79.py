# problem link: https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_r = len(board)
        num_c = len(board[0])
        
        def dfs(r, c, word_seg):
            if len(word_seg) == 1 and board[r][c] == word_seg[0]: 
                return True
            if word_seg[0] == board[r][c]:     
                visited[r][c] = True
                for [i, j] in [[-1, 0], [1, 0], [0, -1], [0, 1]]:   # 递归
                    next_r, next_c = r + i, c + j
                    if 0 <= next_r < num_r and 0 <= next_c < num_c and not visited[next_r][next_c]:
                        if dfs(next_r, next_c, word_seg[1:]):
                            return True
                visited[r][c] = False
            return False
        
        visited = [[False] * num_c for _ in range(num_r)]
        for r in range(num_r):
            for c in range(num_c):
                if board[r][c] == word[0]:
                    if dfs(r, c, word):
                        return True
        return False