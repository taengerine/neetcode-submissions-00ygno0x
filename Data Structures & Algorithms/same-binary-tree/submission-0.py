# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # base case: check if empty 
        if not p and not q:      # empty trees (technically equal)  
            return True     
        if not p or not q or p.val != q.val:       # one is empty 
            return False 

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
