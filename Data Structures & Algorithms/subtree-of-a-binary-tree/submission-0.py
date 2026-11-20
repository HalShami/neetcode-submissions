# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #goal: check if any node in the tree is equal to and has children in subroot. 

        #implementation: 
            #iterate through tree in bfs fashion. If a node == subroot, check if children are equal recursively with bfs. 

        childQueue = deque([root])

        while len(childQueue) != 0:
            node = childQueue.popleft()
            if node.right:
                childQueue.append(node.right)
            if node.left:
                childQueue.append(node.left)
            if node.val == subRoot.val:
                if self.equalTrees(node, subRoot):
                    return True
        return False


    def equalTrees(self, p, q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.equalTrees(p.left, q.left) and self.equalTrees(p.right, q.right)
        else:
            return False

