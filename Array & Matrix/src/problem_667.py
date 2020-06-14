# problem link: https://leetcode.com/problems/beautiful-arrangement-ii/

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = [1]
        for i in range(1, k + 1):
            if i % 2 == 1:
                ans.append(ans[-1] + (k + 1 -i))
            else:
                ans.append(ans[-1] - (k + 1 -i))
        for j in range(n - (k+1)):
            ans.append(k + j + 2)
        return ans