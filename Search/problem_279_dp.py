# problem link: https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(1, int(n**0.5)+1)]
        dp = [float('inf')] * (n+1)
        dp[0] = 0    
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:    # discard squares that are too big
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        return dp[-1]