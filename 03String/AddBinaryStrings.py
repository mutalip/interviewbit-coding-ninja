# Add Binary Strings
# Asked in:  
# Facebook
# Given two binary strings, return their sum (also a binary string).

# Example:

# a = "100"

# b = "11"
# Return a + b = “111”.


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        return str(bin(int(A, 2) + int(B, 2)))[2:]
