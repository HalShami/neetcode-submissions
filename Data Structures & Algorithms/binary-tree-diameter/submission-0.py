# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #approach: keep list of diameters. Take max at the end
        #making list of diameters:
        #   recursively check nodes. Each check should add max length of left + max length of right and save that.
        #   
        if not root:
            return 0

        
        length = self.depth(root.left) + self.depth(root.right)


        return max(self.diameterOfBinaryTree(root.left), length, self.diameterOfBinaryTree(root.right))

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_node = self.depth(root.left)
        right_node = self.depth(root.right)

        return 1 + max(left_node, right_node)