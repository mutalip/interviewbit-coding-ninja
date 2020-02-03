# Min Depth of Binary Tree
# Asked in:  
# Facebook
# Amazon
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

#  NOTE : The path has to end on a leaf node. 
# Example :

#          1
#         /
#        2
# min depth = 2.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        if root.right is None:
            return self.minDepth(root.left)+1
        elif root.left is None:
            return self.minDepth(root.right)+1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
    # def minDepth(self, root):
    #     if not root:
    #         return 0
    #     if not root.left:
    #         return self.minDepth(root.right) + 1
    #     elif not root.right:
    #         return self.minDepth(root.left) + 1
    #     else:
    #         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    
