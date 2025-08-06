class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def has_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Test
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = a  # Creates a loop

print("Loop detected:", has_loop(a))
