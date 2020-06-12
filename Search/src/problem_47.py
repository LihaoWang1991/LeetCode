# problem link: https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        visited = [False] * len(nums)
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                if not visited[i]:
                    if i > 0 and nums[i] == nums[i-1] and visited[i-1] == False: 
                        continue
                    visited[i] = True
                    dfs(path + [nums[i]])
                    visited[i] = False
        dfs([])
        return res