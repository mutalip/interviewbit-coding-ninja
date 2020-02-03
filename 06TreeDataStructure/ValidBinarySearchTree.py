# Valid Binary Search Tree
# Asked in:  
# Amazon
# Facebook
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# Both the left and right subtrees must also be binary search trees.
# Example :

# Input : 
#    1
#   /  \
#  2    3

# Output : 0 or False


# Input : 
#   2
#  / \
# 1   3

# Output : 1 or True 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValid(self,node,mini,maxi):
        
        if node is None:
            return 1
            
        if node.val > maxi or node.val< mini:
            return 0
            
        return (self.isValid(node.left,mini,node.val-1) and self.isValid(node.right,node.val+1,maxi))
            

    def isValidBST(self, A):
        return self.isValid(A,-99999999,99999999)
        
        
