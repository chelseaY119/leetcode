# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if not root:
            return []
        
        result = []
        queue = deque([root]) #initialize the queue with root node

        while queue:
            level = len(queue) # no. of nodes in the current level
            for i in range(level):
                node = queue.popleft() #remove the front node
                if i == level - 1: # last node, save to result
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

        