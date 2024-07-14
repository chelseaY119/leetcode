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


# no.203 remove linklist element
class removeElement(object):
    def solution(self, head, val):
        prevPointer = None
        nextPointer = head
        while nextPointer != None:
            if nextPointer.val != val:
                prevPointer = nextPointer
                if nextPointer.next != None:
                    nextPointer = nextPointer.next
                else:
                    break
            elif (nextPointer.val == val) & (prevPointer == None):
                nextPointer = nextPointer.next
                head = nextPointer
            elif (nextPointer.val == val) & (prevPointer.next != None):
                prevPointer.next = nextPointer.next
                if nextPointer.next != None:
                    nextPointer = nextPointer.next
                else:
                    break
        return head


# no.203 solution with dummy head
class removeElement2(object):
    def solution(self, head, val):
        dummy = Node(0)
        dummy.next = head
        pre = dummy
        next = head

        while next != None:
            if next.val == val:
                pre.next = next.next
            else:
                pre = next
            next = next.next

        return dummy.next


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


# Create a linked list and append some nodes
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(1)

re = removeElement2()
s = re.solution(ll.head, 1)

# Print the linked list
print("\nresult printed")

ll.print_list()
