# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False

        remaining = targetSum - root.val 
        
        if not root.left and not root.right:        # leaf node 
            return remaining == 0                   # return true if equal 
        if self.hasPathSum(root.left, remaining):
            return True
        if self.hasPathSum(root.right, remaining):
            return True 
        
        return False 
