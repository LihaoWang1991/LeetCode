# problem link: https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        old_r = len(nums)
        old_c = len(nums[0])
        if r * c != old_r * old_c:
            return nums
        new_nums = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                new_nums[i][j] = nums[(i * c + j) // old_c][(i * c + j) % old_c]
        return new_nums