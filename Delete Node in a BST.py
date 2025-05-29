# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minValue(self, root):
        curr = root

        while curr and curr.left:
            curr = curr.left

        return curr

    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            else:
                min = self.minValue(root.right)
                root.val = min.val
                root.right = self.deleteNode(root.right, min.val)

        return root
        