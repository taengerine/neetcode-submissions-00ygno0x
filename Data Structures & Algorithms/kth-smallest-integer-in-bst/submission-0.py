# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        value = 0 
        order = 0 
        def bst(root):
            nonlocal value, order
            if not root:
                return 

            bst(root.left)
            order += 1
            if order == k: 
                value = root.val
                return 
            bst(root.right)
        bst(root)
        return value 

  
        