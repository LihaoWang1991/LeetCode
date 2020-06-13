# problem link: https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(cur_list, next_ind):
            if sum(cur_list) == target:
                res.append(cur_list)
                return
            if sum(cur_list) > target:
                return
            for ind_i in range(next_ind, len(candidates)):
                if ind_i > next_ind and candidates[ind_i] == candidates[ind_i - 1]:    # avoid duplicate results due to equal elements
                    continue
                else:
                    helper(cur_list + [candidates[ind_i]], ind_i + 1)
        
        helper([],0)
        return res