# Square Root of Integer
# Asked in:  
# Facebook
# Amazon
# Microsoft
# Given an integar A.

# Compute and return the square root of A.

# If A is not a perfect square, return floor(sqrt(A)).

# DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY



# Input Format

# The first and only argument given is the integer A.
# Output Format

# Return floor(sqrt(A))
# Constraints

# 1 <= A <= 10^9
# For Example

# Input 1:
#     A = 11
# Output 1:
#     3

# Input 2:
#     A = 9
# Output 2:
#     3
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, x):
        # Base cases 
        if (x == 0 or x == 1) : 
            return x 
       
        # Do Binary Search for floor(sqrt(x)) 
        start = 1
        end = x    
        while (start <= end) : 
            mid = (start + end) // 2
              
            # If x is a perfect square 
            if (mid*mid == x) : 
                return mid 
                  
            # Since we need floor, we update  
            # answer when mid*mid is smaller 
            # than x, and move closer to sqrt(x) 
            if (mid * mid < x) : 
                start = mid + 1
                ans = mid 
                  
            else : 
                  
                # If mid*mid is greater than x 
                end = mid-1
                  
        return ans 
