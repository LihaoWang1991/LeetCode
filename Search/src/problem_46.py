# problem link: https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(list_done, list_to_do, num_done):
            if num_done == len(nums):
                res.append(list_done)
                return
            for i in range(len(list_to_do)):
                dfs(list_done + [list_to_do[i]], list_to_do[:i] + list_to_do[i+1:], num_done+1)

        dfs([], nums, 0)
        return res