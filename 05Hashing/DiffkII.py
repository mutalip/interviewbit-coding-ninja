# Diffk II
# Asked in:  
# Facebook
# Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

# Example :

# Input :

# A : [1 5 3]
# k : 2
# Output :

# 1
# as 3 - 1 = 2

# Return 0 / 1 for this problem.



class Solution:
    def diffPossible(self, A, B):
        mapp={}
        for x in A:
            if mapp.get(x+B,False)==True or mapp.get(x-B,False)==True:
                return 1
            mapp[x]=True
        return 0
        
        # for i in range (len(A)):
        #     for j in range(i+1,len(A)):
        #         if A[i]-A[j]==B or A[j]-A[i]==B:
        #             return 1
        # return 0
        
