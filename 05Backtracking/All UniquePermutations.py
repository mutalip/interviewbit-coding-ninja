# All Unique Permutations
# Asked in:  
# Microsoft
# Facebook
# Google
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Example :
# [1,1,2] have the following unique permutations:

# [1,1,2]
# [1,2,1]
# [2,1,1]
#  NOTE : No 2 entries in the permutation sequence should be the same. 
#  Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. Example : next_permutations in C++ / itertools.permutations in python.
# If you do, we will disqualify your submission retroactively and give you penalty points. 


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
#    def permute(self, A):
    def f(self, A, n):
        if n == len(A):
            return [list(A)]
        else:
            ans = []
            s = set()
            ans += self.f(A, n + 1)
            s.add(A[n])
            for i in range(n+1, len(A)):
                if A[i] not in s:
                    A[n], A[i] = A[i], A[n]
                    ans += self.f(A, n + 1)
                    A[n], A[i] = A[i], A[n]
                    s.add(A[i])
            return ans

    # @return a list of list of integers
    def permute(self, A):
        return self.f(A, 0)
