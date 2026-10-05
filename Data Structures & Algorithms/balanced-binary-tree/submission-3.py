# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #approach: recurse through sub-trees while checking that |len(right_tree) - len(left_tree)| <= 1. If not equal, return false. If recursion ends, return true


        #Goal: iterate to bottom of each subtree and check if it's subtrees are balanced. If they are, continue up without returning False


        if not root:
            return True

        left_len = self.depth(root.left)
        right_len = self.depth(root.right)
        
        if abs(left_len - right_len) > 1:
            return False


        return (self.isBalanced(root.left) and self.isBalanced(root.right))

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_node = self.depth(root.left)
        right_node = self.depth(root.right)

        return 1 + max(left_node, right_node)