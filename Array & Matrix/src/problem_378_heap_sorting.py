# problem link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        heap = []
        nums = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                nums.append(-matrix[r][c])
        return -heapq.nlargest(k, nums)[-1]