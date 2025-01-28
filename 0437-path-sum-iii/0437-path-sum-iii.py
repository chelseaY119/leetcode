# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def count_path_from_node(node, targetSum):
            if not node:
                return 0
            
            count = 1 if node.val == targetSum else 0
            
            count += count_path_from_node(node.left, targetSum - node.val)
            count += count_path_from_node(node.right, targetSum - node.val)
            
            return count
        
        if not root:
            return 0
        
        return count_path_from_node(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
            









        