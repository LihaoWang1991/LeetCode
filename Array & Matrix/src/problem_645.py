# problem link: https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0, 0]
        n = len(nums)
        nums_sum = sum(nums)
        nums_set = set(nums)
        good_sum = int((1 + n) / 2 * n)
        for i in range(1, n+1):
            if i not in nums_set:
                ans[1] = i
        ans[0] = ans[1] - (good_sum - nums_sum)
        return ans