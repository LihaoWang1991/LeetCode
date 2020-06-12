# problem link: https://leetcode.com/problems/binary-tree-paths/

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def dfs(node, prev_path):
            if not node:
                return
            cur_path = prev_path + str(node.val)
            if not node.left and not node.right:
                res.append(cur_path)
                return
            for next_node in [node.left, node.right]:
                dfs(next_node, cur_path + "->")
        dfs(root, "")
        return res