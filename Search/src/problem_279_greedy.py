# problem link: https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = set([i * i for i in range(1, int(n**0.5)+1)])
        def can_be_split(n, count):
            if count == 1:
                return n in square_nums
            for k in square_nums:
                if n - k > 0 and can_be_split(n - k, count - 1):
                    return True
            return False
    
        for count in range(1, n+1):
            if can_be_split(n, count):
                return count