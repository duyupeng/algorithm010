"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections  import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        queue=deque([root])
        result=[]
        while queue:
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)
        return result