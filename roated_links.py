# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or not k: return head
        num = 0
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        p2 = dummy
        # 计算个数
        while p1.next:
            num += 1
            p1 = p1.next
        #print(num)
        # 找前一段链表
        k = num - k % num
        #print(k)
        while k :
            p2 = p2.next
            k -= 1
        
        # 连接
        p1.next = dummy.next
        dummy.next = p2.next
        p2.next = None
        
        return dummy.next
        