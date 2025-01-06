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


# no.160 intersaction of two linkedlist
class intersectionOfTwoLL(object):
    def solution(self, headA, headB):
        curA = headA
        curB = headB
        lenA, lenB, diff = 0

        while curA:
            lenA += 1
            curA = curA.next

        while curB:
            lenB += 1
            curB = curB.next
        curA, curB = headA, headB

        if lenA > lenB:
            diff = lenA - lenB

        else:
            diff = lenB - lenA
            curA, curB = headB, headA

        while diff > 0:
            curA = curA.next
            diff -= 1

        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next

        return None
