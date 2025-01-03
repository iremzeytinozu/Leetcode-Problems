# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        queue = deque()

        if not root:
            return []

        queue = deque([root])
        result = []

        while queue: # queue bosalana kadar

            height = len(queue)
            list = []

            for _ in range(height):

                current = queue.popleft()
                list.append(current.val)

                if current.left:
                    queue.append(current.left)
                
                if current.right:
                    queue.append(current.right)

            result.append(list)

        return result

        