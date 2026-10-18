# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #goal: return array containing lists of values of nodes one level at a time

        #implementation: Use BFS approach with Queue. Loop through all elements in queue at every level and add their values to do level-by level
        if not root:
            return []

        NodesQueue = deque([root])
        retList = []

        while len(NodesQueue) != 0:
            #add values in NodesQueue to retList before moving on to next level
            levelList = []
            for value in NodesQueue:
                levelList.append(value.val)
            retList.append(levelList)
            #iterate through values in queue at the current level & perform logic then add their children to end of queue
            for i in range(len(NodesQueue)):
                Node = NodesQueue.popleft()
                if Node.left:
                    NodesQueue.append(Node.left)
                if Node.right:
                    NodesQueue.append(Node.right)

        return retList




