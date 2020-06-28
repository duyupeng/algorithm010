# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root) -> bool:

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node: return True
            val = node.val
            if val <= lower or val >= upper: return False
            left = helper(node.left, lower, val)
            right = helper(node.right, val, upper)
            if not left: return False
            if not right: return False
            return True

        return helper(root)