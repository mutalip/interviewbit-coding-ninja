# Given an unsorted integer array, find the first missing positive integer.

# Example:

# Given [1,2,0] return 3,

# [3,4,-1,1] return 2,

# [-8, -7, -6] returns 1

# Your algorithm should run in O(n) time and use constant space.

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A.sort()
        for i in range(0,len(A)):
            if(A[i]>0):
                break
        A = A[i:]
        if(A[0]!=1):
            return 1
        for i in range(1,len(A)):
            if(A[i] - A[i-1]!=1):
                return A[i-1]+1
        return A[i]+1
