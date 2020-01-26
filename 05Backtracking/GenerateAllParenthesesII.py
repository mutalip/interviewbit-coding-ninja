# Generate all Parentheses II
# Asked in:  
# Facebook
# Microsoft
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

# For example, given n = 3, a solution set is:

# "((()))", "(()())", "(())()", "()(())", "()()()"
# Make sure the returned list of strings are sorted.

class Solution:
    # @param A : integer
    # @return a list of strings
#    def generateParenthesis(self, A):
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left,right, ans, "")
        return ans
    
    def dfs(self, left, right, ans, string):
        if right < left:
            return
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left-1, right, ans, string + "(")
        if right:
            self.dfs(left, right-1, ans, string + ")")
