# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def append_front(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        temp = None
        while current:
            temp = append_front(temp, current.val)
            current = current.next
        return temp
        