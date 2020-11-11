'''
Recursive--------------------Solution-----------------------
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [1,2]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        tree = []
        if not root:
            return []
        
        elif root == []:
            return []
        
        def helper(node):
            if not node:
                return 
            tree.append(node.val)
            left = helper(node.left)
            right = helper(node.right)
            return tree
        
        return helper(root)
        
        '''
        *** Code beats 93.58% Python3 submissions ***
        '''
