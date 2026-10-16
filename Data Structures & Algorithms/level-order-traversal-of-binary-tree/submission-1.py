# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Process to BFS through a tree:
        #1. initialize queue to contain root ode
        #2. loop through all values in queue
        #       append values in queue to current_level list by popping
        #       append node.left and node.right to queue 
        #3. append current_level values to results & continue to loop through the queue

        if not root:
            return []
        queue = deque([root])

        retList=[]

        while queue:
            levelList = []
            for i in range(len(queue)):
                node = queue.popleft()
                levelList.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            retList.append(levelList)
        return retList