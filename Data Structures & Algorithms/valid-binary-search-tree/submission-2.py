# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, interval):
            if not node:
                return True

            if not (interval[0] < node.val < interval[1]):
                return False
            
            left = dfs(node.left, [interval[0], node.val])
            right = dfs(node.right, [node.val, interval[1]])

            return left and right

        return dfs(root, [float('-inf'), float('inf')])

        




        