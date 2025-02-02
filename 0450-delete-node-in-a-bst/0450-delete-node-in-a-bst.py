# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key) # check left side
        elif key > root.val:
            root.right = self.deleteNode(root.right, key) # check right side
        else: # key == root.val
            # only one child / no child
            if not root.left: # with no left child
                return root.right
            elif not root.right: # with no right child 
                return root.left

            # both child 
            min_node = self.helper(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        return root

    # helper node for finding the smaller node on the right side, so it can be replaced with the deleted node
    def helper(self, root):
        while root.left:
            root = root.left
        return root
