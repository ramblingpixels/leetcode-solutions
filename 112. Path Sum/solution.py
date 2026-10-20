# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        def dfs(root, targetSum):
            if not root:
                return False

            if not root.left and not root.right:
                return root.val == targetSum
            
            path_sum_left = dfs(root.left, targetSum - root.val)
            path_sum_right = dfs(root.right, targetSum - root.val)

            return path_sum_left or path_sum_right
        
        return dfs(root,targetSum)