# Diffk

#     Asked in:  
#     Facebook

# Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

#     Example:

#     Input : 

#     A : [1 3 5] 
#     k : 4

#     Output : YES

#     as 5 - 1 = 4 

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

# Try doing this in less than linear space complexity.



class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A)<2:
            return 0
        i=0
        j=1
        while j<len(A) and i<len(A):
            if A[j]-A[i]-B == 0 and i!=j:
                return 1
            elif A[j]-A[i]-B >0:
                i+=1
            elif A[j]-A[i]-B <0:
                j+=1
            else :
                j+=1
        return 0
