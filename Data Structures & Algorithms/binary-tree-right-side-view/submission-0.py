# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #same approach as breadth-first layer by layer traversal. Just take output and only keep rightmost value in each layer's sublist

        queue = deque([root])

        retList = []

        if not root:
            return []

        while queue:
            layerList = []
            for i in range(len(queue)):
                node = queue.popleft()
                layerList.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            retList.append(layerList)

        retList2 = []
        for layerList in retList:
            retList2.append(layerList.pop())

        return retList2