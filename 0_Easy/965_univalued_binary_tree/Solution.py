# 965. Univalued Binary Tree

# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def traverse(n):
            if n.val != root.val:
                return False
            ret = True
            if n.left:
                ret = ret and traverse(n.left)
            if n.right:
                ret = ret and traverse(n.right)
            return ret
        return traverse(root)
