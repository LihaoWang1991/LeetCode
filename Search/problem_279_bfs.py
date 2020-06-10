# problem link: https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = set([i * i for i in range(1, int(n**0.5)+1)])
        cur_cnt = 1
        queue = {n}
        while True:
            new_queue = set()
            for i in queue:
                if i in square_nums:
                    return cur_cnt
                else:
                    for j in square_nums:
                        if i - j < 0:
                            continue
                        new_queue.add(i - j)
            cur_cnt += 1
            queue = new_queue