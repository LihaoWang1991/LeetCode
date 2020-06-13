# problem link: https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        end_num = 10  # candidates numbers are btw 0 - 9
        def dfs(cur_list, cur_size, next_num):
            if cur_size == k and sum(cur_list) == n:
                res.append(cur_list)
                return
            if cur_size > k or sum(cur_list) > n:   # pruning
                return
            for i in range(next_num, end_num):
                dfs(cur_list + [i], cur_size + 1, i + 1)
        res = []
        dfs([], 0, 1)
        return res