# problem link: https://leetcode.com/problems/degree-of-an-array/

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ans = float("inf")
        start = {}
        end = {}
        cnt = {}
        for i in range(len(nums)):
            if nums[i] not in start:
                start[nums[i]] = i
            cnt[nums[i]] = cnt.get(nums[i], 0) + 1
            end[nums[i]] = i
        max_cnt = max(cnt.values())
        for i in cnt:
            if cnt[i] == max_cnt:
                ans = min(ans, end[i] - start[i] + 1)
        return ans