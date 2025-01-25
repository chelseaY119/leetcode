# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        prev = None
        while current != None:
            temp = current.next # store the next node
            current.next = prev # reverse the link
            prev = current # move the pre to current node
            current = temp # move current node to next node
        
        return prev


        