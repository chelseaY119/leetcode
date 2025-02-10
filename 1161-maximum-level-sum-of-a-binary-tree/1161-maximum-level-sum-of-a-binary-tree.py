# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = deque([root]) # initialize queue with root node
        max_level = 1
        level = 1
        max_sum = float('-inf')
        
        while queue:
            summ = 0
            size = len(queue) # no. of nodes in current level
            for _ in range(size):
                node = queue.popleft() # remove the front node 
                summ += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if summ > max_sum: 
                max_sum = summ
                max_level = level
            
            level += 1
                    
        return max_level


        