# Regular Expression II
# Asked in:  
# Facebook
# Microsoft
# Google
# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:

# int isMatch(const char *s, const char *p)
# Some examples:

# isMatch("aa","a") → 0
# isMatch("aa","aa") → 1
# isMatch("aaa","aa") → 0
# isMatch("aa", "a*") → 1
# isMatch("aa", ".*") → 1
# isMatch("ab", ".*") → 1
# isMatch("aab", "c*a*b") → 1
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


#class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
#    def isMatch(self, A, B):
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    # dp[i][j] does i chars of b match j chars of a
     def isMatch(self, A, B, index_s=0, index_r=0):
        while index_s < len(A) and index_r < len(B):
            if B[index_r] == '.':
                if index_r + 1 < len(B) and B[index_r+1] == '*':
                    for i in range(index_s, len(A)+1):
                        if self.isMatch(A, B, i, index_r+2):
                            return 1
                    return 0
                else:
                    index_s += 1
                    index_r += 1
            else:
                ch = B[index_r]
                if index_r + 1 < len(B) and B[index_r+1] == '*':
                    for i in range(index_s, len(A)+1):
                        if i > index_s and A[i-1] != ch:
                            break
                        if self.isMatch(A, B, i, index_r+2):
                            return 1
                    return 0
                else:
                    if ch == A[index_s]:
                        index_r += 1
                        index_s += 1
                    else:
                        return 0
        if index_s == len(A) and index_r == len(B):
            return 1
        if index_s == len(A) or index_r == len(B):
            return 0
