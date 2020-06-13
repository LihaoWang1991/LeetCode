# problem link: https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur_list, next_idx):
            res.append(cur_list.copy())
            for i in range(next_idx, len(nums)):
                cur_list.append(nums[i])
                dfs(cur_list, i + 1)
                cur_list.pop()
        dfs([],0)
        return res