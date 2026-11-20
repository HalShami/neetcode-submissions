# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #traverse through all elements in both trees alternating in same order and check if they are each the same

        #we will do dfs traversal. Actually nah it will be hard to build adjacency list with recursion involved. 
        #I think two approaches: 1. Build adjacency list and compare them both at end. 2. iterate elements on p then on q and compare in same order 1 at a time. 

        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


