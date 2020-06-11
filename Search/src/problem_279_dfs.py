# problem link: https://leetcode.com/problems/perfect-squares/
# The DFS method will exceed time limit.

class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = {i**2 for i in range(1, int(n**0.5)+1)}
        self.res = float("inf")
        def helper(num, cnt):
            if num in square_nums:    
                cnt += 1
                self.res = min(self.res, cnt)
                return
            for i in square_nums:
                if num - i > 0:
                    helper(num - i, cnt + 1)
        helper(n, 0)
        return self.res