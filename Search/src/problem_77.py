# problem link: https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        visited = [False] * n
        res = []
        def backtrack(path):
            if len(path) == k:
                res.append(path)
                return
            start = path[-1] if path else 0
            for i in range(start, n):
                if not visited[i]:
                    visited[i] = True
                    backtrack(path + [i+1])
                    visited[i] = False
        backtrack([])
        return res