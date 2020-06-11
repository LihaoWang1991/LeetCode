# problem link: https://leetcode.com/problems/friend-circles/

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        stat_visited = [0 for _ in range(n)]
        ans = 0
        def dfs(i):    # i is the index of student
            if stat_visited[i] == 1:
                return
            stat_visited[i] = 1
            for j in range(n):
                if M[i][j] == 1:
                    dfs(j)
                
        for i in range(n):
            if stat_visited[i] == 0: 
                ans += 1
                dfs(i)
        return ans