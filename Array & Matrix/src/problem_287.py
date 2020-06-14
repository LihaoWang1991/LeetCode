# problem link: https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt > mid:
                high = mid - 1
            else:
                low = mid + 1
        return low