# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #利用二叉搜索树的左子树所有节点小于root,右子树所有节点大于root的特性
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val<root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q) #均在左子树
        if p.val>root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)#均在右子树
        return root #否则p,q分布在左右直接返回root
