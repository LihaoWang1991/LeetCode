# problem link: https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def dfs(prev_s, later_s, i):   # i means the order of the segment in the IP address 
            if later_s == "":    # illegal case
                return
            if i == 4:
                if later_s[0] == "0" and len(later_s) > 1:   
                    return
                elif 0 <= int(later_s) <= 255:
                    ans.append(prev_s + later_s)
                else:
                    return
            else:
                if later_s[0] == "0":   # if one segment starts with 0 then the 0 must be treated as one segment
                    dfs(prev_s + later_s[0] + ".", later_s[1:], i + 1)
                else:
                    for j in range(min(3, len(later_s))):
                        if j == 2 and int(later_s[0:3]) > 255:
                            continue
                        dfs(prev_s + later_s[0:j+1] + ".", later_s[j+1:], i+1) 
        dfs("", s, 1)
        return ans