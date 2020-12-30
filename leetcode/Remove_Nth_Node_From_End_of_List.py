# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        num=0
        copy=None
        while head!=None:
            copy=ListNode(head.val,copy)
            head=head.next
            num+=1
        out=None
        for i in range(num):
            if i !=n-1:
                out=ListNode(copy.val,out)
                copy=copy.next
            else:
                copy=copy.next
        return out
        