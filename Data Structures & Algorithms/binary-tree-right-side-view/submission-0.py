# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque() 
        result = []

        if root:
            queue.append(root)
            #result.append(root.val)
        
        while len(queue) > 0:
            nums = []           # list for each level nums 
            for i in range(len(queue)):
                curr = queue.popleft()
                nums.append(curr.val)
                if curr.left: 
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(nums[-1])     # very rightside of the number
        
        return result 