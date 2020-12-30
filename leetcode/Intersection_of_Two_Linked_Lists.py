# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def length(L):
            length=0
            while L:
                length+=1
                L=L.next
            return length
        l0,l1=headA,headB
        l0_len,l1_len=length(l0),length(l1)
        if l0_len>l1_len:
            l0,l1=l1,l0
        for i in range(abs(l0_len-l1_len)):
            l1=l1.next
        while l0 and l1 and l0 is not l1:
            l0,l1=l0.next,l1.next
        return l0
            
        