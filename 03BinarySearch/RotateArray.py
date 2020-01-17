# Rotated Array
# Asked in:  
# Facebook
# Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# The array will not contain duplicates.

# NOTE 1: Also think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
# PROBLEM APPROACH:

# Note: If you know the number of times the array is rotated, then this problem becomes trivial. If the number of rotation is x, then minimum element is A[x].
# Lets look at how we can calculate the number of times the array is rotated.

# Complete solution in the hints.



#class Solution:
    # @param A : tuple of integers
    # @return an integer
#    def findMin(self, A):
class Solution:
    # @param A : tuple of integers
    # @return an integer
    
    def searchMin(self, A, low, high):
        
        if low == high:
            return A[low]
        
        mid = low + ((high-low) // 2)
        
        if A[mid] < A[high]:
            return self.searchMin(A, low, mid)
        else:
            return self.searchMin(A, mid+1, high)
        
        
    def findMin(self, A):
        return self.searchMin(A, 0, len(A)-1)
