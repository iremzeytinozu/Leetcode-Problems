# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        
        result = []
        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            level_length = len(queue)

            for i in range(level_length):
                curr = queue.popleft()

                if i == level_length - 1:
                    result.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)   
        
        return result
