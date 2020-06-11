# problem link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        if digits == '':
            return []
        res = []
        
        def dfs(comb, ind):
            if ind == len(digits):
                res.append(comb)
                return
            for letter in words[int(digits[ind]) - 2]:
                dfs(comb + letter, ind + 1)
                     
        dfs('',0)
        return res