# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #recurse through tree using dfs until you hit bottom. return 1 + recursive call
        if not root:
            return 0

        return max((1 + self.maxDepth(root.left)), (1+self.maxDepth(root.right)))
