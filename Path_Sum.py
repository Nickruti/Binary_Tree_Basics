'''
Problem url - https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
'''

#------------ My Naive Solution --------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        sum_ = 0
        def helper(node, sum, sum_):
            if node is None:
                return 
            if (node.left is None) and (node.right is None):
                sum_ += node.val
                if sum_ == sum:
                    return True
                return False
            sum_ = sum_ + node.val
            return helper(node.left, sum, sum_) or helper(node.right, sum, sum_)
            
        return helper(root, sum, sum_)
            
#------------- Best Solution -----------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, num: int) -> bool:
        if root is None:
            return False
        elif not root.left and not root.right:
            return (root.val == num)
        elif not root.left:
            return self.hasPathSum(root.right, num-root.val)
        elif not root.right:
            return self.hasPathSum(root.left, num-root.val)
        else:
            return self.hasPathSum(root.right, num-root.val) or self.hasPathSum(root.left, num-root.val)
