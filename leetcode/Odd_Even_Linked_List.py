# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        front = head
        tail = cur = head.next  # use cur to iterate the original list
        while(cur and cur.next):  # may end at a odd node or end at an even node           
            front.next = cur.next
            front = front.next
            cur.next = cur.next.next
            cur = cur.next
        front.next = tail
        return head
                
                
        
        
        