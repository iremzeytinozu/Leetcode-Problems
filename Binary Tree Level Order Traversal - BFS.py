# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def levelOrder(self, root):

        result = []
        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            level = []

            for i in range(len(queue)):
                curr = queue.popleft()

                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)

            if level:
                result.append(level)     
        
        return result