# problem link: https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(cur_list, next_ind):
            if sum(cur_list) == target:
                res.append(cur_list)
                return
            if sum(cur_list) > target:   # pruning
                return
            for ind_i in range(next_ind, len(candidates)):  # avoid duplicate results
                helper(cur_list + [candidates[ind_i]], ind_i)
        helper([],0)
        return res