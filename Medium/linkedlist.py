# no 707 design linkedlist
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):
    def __init__(self):
        self.dummy_head = Node(0)
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        count = index
        current = self.dummy_head.next
        while count > 0:
            current = current.next
            count -= 1

        return current.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.dummy_head.next = Node(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current = self.dummy_head
        while current.next != None:
            current = current.next
        current.next = Node(val)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return

        count = index
        current = self.dummy_head

        while count > 0:
            current = current.next
            count -= 1
        current.next = Node(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        count = index
        current = self.dummy_head

        while count > 0:
            current = current.next
            count -= 1
        current.next = current.next.next
        self.size -= 1


# no 24 swap nodes in linkedlist
class swapNodes(object):
    def solution(self, head):
        dummy = Node(next=head)
        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next

            first.next = second.next
            cur.next = second
            second.next = first

            cur = first

        return dummy.next


# no 19 remove nth node from end of list
class removeNNode(object):
    def solution(self, head, n):
        # use a dummy head that point to real head node
        dummy = Node(0)
        dummy.next = head
        slow = dummy
        fast = slow

        while n >= 0:
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next
        if slow.next == None:
            slow.next = fast
        else:
            slow.next = slow.next.next

        return dummy.next


# no.142 circular linkedlist
