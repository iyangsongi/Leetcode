# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        思路：使用递归+DFS思想，终止条件为root==null,逐层返回，每层加一
        """
        if not root:return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1