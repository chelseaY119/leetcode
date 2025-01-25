# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head.next or not head:
            return None

        slow = head # a slow pointer that moves one at a time
        fast = head # a fast pointer that moves two at a time
        prev = None

        while fast and fast.next: # when fast pointer reach the end of the ll
            prev = slow # move the prev node to slow
            slow = slow.next # move slow node by 1
            fast = fast.next.next # move fast node by 2
        
        if prev:
            prev.next = slow.next

        return head 
    





        