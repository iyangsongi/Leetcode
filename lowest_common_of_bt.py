# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:return root
        if root==q or root ==p:return root
        left= self.lowestCommonAncestor(root.left,p,q)
        right= self.lowestCommonAncestor(root.right,p,q)
        if not left:
            return right
        elif not right:
            return left
        else:
            return root #表示左右子树分布在root左右那么可以判定root为最近祖先
