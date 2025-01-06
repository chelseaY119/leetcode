# Definition for singly-linked list.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# use for testing code purpose
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")


# no 206
class reverseLinkedlist(object):
    def solution(self, head):
        cur = head
        pre = None
        temp = None
        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre
