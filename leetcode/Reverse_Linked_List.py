####################Recursive Method##############
class Solution:
    def helper(self,prev,curr):
        if curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            return self.helper(prev,temp)
        else:
            return prev
    
    def reverseList(self, head: ListNode) -> ListNode:
        return self.helper(None,head)
        #1->2->3->4->X


#############Iterative Method###################
class Solution:
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        curr=head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev