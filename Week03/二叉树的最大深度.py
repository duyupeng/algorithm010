# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root) -> int:
        if not root: return 0
        root_left=self.maxDepth(root.left)
        root_right=self.maxDepth(root.right)
        return max(root_left,root_right)+1