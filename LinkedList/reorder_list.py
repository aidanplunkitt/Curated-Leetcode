# https://leetcode.com/problems/reorder-list/
# O(n) time, O(1) space

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + ' -> ' + (self.next.__repr__() if self.next else 'None')

def reorder_list(head):
    """
    Do not return anything, modify head in-place instead.
    """
    if not head: return None

    # find mid
    mid = tail = head
    while tail and tail.next:
        mid = mid.next
        tail = tail.next.next
        
    # reverse mid to tail
    prev = None
    while mid:
        mid.next, prev, mid = prev, mid, mid.next
 
    # merge linked lists
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next

    return head

def make_list(a):
    curr = dhead = ListNode()
    for e in a:
        curr.next = ListNode(e)
        curr = curr.next
    return dhead.next

l = make_list([1,2,3,4,5])
print("Before:", l)
reorder_list(l)
print("After:", l)