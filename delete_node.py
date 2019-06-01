# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        官方题解：我们无法访问我们想要删除的节点之前的节点，但我们可以将当前值替换为下一个值
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val;
        node.next = node.next.next;