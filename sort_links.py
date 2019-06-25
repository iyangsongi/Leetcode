# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if(head is None or head.next is None):
            return head
        pre=head
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            pre=slow
            slow=slow.next
            fast=fast.next.next
        left=head
        right=pre.next
        pre.next=None
        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)
    
    def merge(self,left,right):
        head=ListNode(0)
        pre=head
        while(left and right):
            if(left.val<right.val):
                pre.next=left
                pre=left
                left=left.next
            else:
                pre.next=right
                pre=right
                right=right.next
        if(left is None):
            pre.next=right
        else:
            pre.next=left
        return head.next
        