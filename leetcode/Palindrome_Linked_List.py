# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(L):
            copy=None
            while L:
                copy=ListNode(L.val,copy)
                L=L.next
            return copy
        
        
        slow=fast=head
        while fast and fast.next and fast.next.next:
            slow,fast=slow.next,fast.next.next
        first_half=head
        sec_half=reverse(slow)
        while first_half and sec_half:
            if first_half.val != sec_half.val:
                return False
            else:
                first_half,sec_half=first_half.next,sec_half.next
        return True
        
        