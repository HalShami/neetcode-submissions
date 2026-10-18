# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #goal: traverse through the tree one level at a time & put all values at that level in a list. Append that list to retList

        retList = []

        #Implementation: BFS traversal through tree using queue. No need for visited set since we never traverse backwards. At start of every level, append values in queue to retList. 
        if not root:
            return []
        levelQueue = deque([root])

        while len(levelQueue) != 0:
            #we need to keep track of every level.
            levelList = []
            for val in levelQueue:
                if val:
                    levelList.append(val.val)
            retList.append(levelList)
            levelSize = len(levelQueue)
            for i in range(levelSize):
                Node = levelQueue.popleft()
                if Node:
                    if Node.left:
                        levelQueue.append(Node.left)
                    if Node.right:
                        levelQueue.append(Node.right)

        return retList
        
