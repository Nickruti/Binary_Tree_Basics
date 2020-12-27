'''
Problem url - https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def helper(root):
            if root is None:
                return 0
            left_ans = helper(root.left)
            right_ans = helper(root.right)
            return max(left_ans, right_ans)+1
        return helper(root)
        
