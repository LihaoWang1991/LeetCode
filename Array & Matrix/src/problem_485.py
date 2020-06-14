# problem link: https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cur_sum = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur_sum += 1
                ans = max(ans, cur_sum)
            else:
                cur_sum = 0
        return ans