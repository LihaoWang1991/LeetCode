# problem link: https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(cur_list, next_idx):
            res.append(cur_list.copy())
            for i in range(next_idx, len(nums)):
                if i > next_idx and nums[i] == nums[i-1]:    # avoid duplicate results due to equal elements
                    continue
                cur_list.append(nums[i])
                dfs(cur_list, i + 1)
                cur_list.pop()
        res = []
        dfs([], 0)
        return res