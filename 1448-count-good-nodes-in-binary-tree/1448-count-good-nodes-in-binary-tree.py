# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def count_good_nodes(root, reference_val):
            if not root:
                return 0
            
            good = 1 if root.val >= reference_val else 0
            reference_val = max(root.val, reference_val)

            good += count_good_nodes(root.left, reference_val)
            good += count_good_nodes(root.right, reference_val)

            return good
        
        return count_good_nodes(root, root.val)


            
        