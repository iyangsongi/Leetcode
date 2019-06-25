# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def gen(r):
            if r is not None:
                yield from gen(r.left)
                yield r.val
                yield from gen(r.right)
        
        it = gen(root)
        for _ in range(k):
            ans = next(it)
        return ans
        