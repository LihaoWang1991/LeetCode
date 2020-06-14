# problem link: https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """"""
        Do not return anything, modify nums in-place instead.
        """"""
        j = 0
        for i in range(len(nums)):
                        # if current element is not 0，exchange it to left side，otherwise exchange it to right side
            if nums[i]:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1