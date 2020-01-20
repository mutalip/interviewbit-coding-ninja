# 3 Sum Zero
# Asked in:  
# Facebook
# Google
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

# Note:

#  Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
# The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
# (-1, 0, 1)
# (-1, -1, 2)


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        if len(A) < 3:
            return []
        A.sort()
        ret = set()
        for i in range(len(A)-2):
            j,k=i+1,len(A)-1
            while j<k:
                tempsum = A[i]+A[j]+A[k]
                if tempsum == 0:
                    ret.add((A[i], A[j], A[k]))
                if tempsum<0:
                    j+=1
                else:
                    k-=1
        return list(ret)
