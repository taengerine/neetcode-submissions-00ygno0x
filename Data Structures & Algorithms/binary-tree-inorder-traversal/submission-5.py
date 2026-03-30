# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = [] 
        if not root:
            return order
            
        #self.inorderTraversal(root.left)
        order = order + self.inorderTraversal(root.left)
        order.append(root.val)
        order = order + self.inorderTraversal(root.right)

        return order

        