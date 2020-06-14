# problem link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low = matrix[0][0]
        high = matrix[-1][-1]
        n = len(matrix)
        def cnt_no_bigger_than_mid(mid):
            cnt = 0         
            r, c = n-1, 0   # begin from the left down corner
            while r >= 0:  
                while c < n and matrix[r][c] <= mid:
                    c += 1
                cnt += c 
                c = max(c - 1, 0)   # avoid c-1 becomes -1 in case c == 0
                r = r - 1
            return cnt
        while low < high:
            mid = (low + high) // 2
            cnt = cnt_no_bigger_than_mid(mid)
            if cnt >= k:
                high = mid
            else:
                low = mid + 1
        return low