# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        
        # helper function to get leaves
        def get_leaves(root):
            if root is None:
                return []
            
            # find the leaf
            if root.left is None and root.right is None:
                return [root.val]
            
            # comtinue find the leaf for the root
            return get_leaves(root.left) + get_leaves(root.right)
        
        leave1 = get_leaves(root1)
        leave2 = get_leaves(root2)

        return leave1 == leave2
            
        

            
        
        
        