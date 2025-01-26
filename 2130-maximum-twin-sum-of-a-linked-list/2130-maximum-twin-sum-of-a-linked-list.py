# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        slow = head
        fast = head
        
        prev = None
        
        max_sum = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next        
        
        # reverse the second half
        prev, curr = None, slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #calculate the pair
        first, second = head, prev
        
        while second:
            max_sum = max(first.val + second.val, max_sum)
            second = second.next
            first = first.next
        
        return max_sum





        