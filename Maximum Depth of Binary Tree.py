# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):

        if not root:
            return 0

        # solu ve sağı karşılaştır en büyüğünü bul root'u almak için 1 ekle
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        