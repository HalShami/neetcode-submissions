# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #goal: switch right child with left child

        #implementation: traverse through the tree in BFS order. After adding children to the queue, add them to a new node's children in reverse order. Return root node at end
        if root == None:
            return None
        childQueue = deque([root])

        while len(childQueue) != 0:
            #4 cases for switching:
            #1. left and right both exist. Just switch
            #2. only left - place left in right
            #3. only right - place right in left
            #4. none - do nothing
            node = childQueue.popleft()
           
            if node.left and node.right:
                tempLeft = node.left
                node.left = node.right
                node.right = tempLeft

            elif node.left:
                node.right = node.left
                node.left = None
            
            elif node.right:
                node.left = node.right
                node.right = None


            if node.left:
                childQueue.append(node.left)
            if node.right:
                childQueue.append(node.right)

        return root
        