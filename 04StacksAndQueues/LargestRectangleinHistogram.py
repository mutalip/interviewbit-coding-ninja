# Largest Rectangle in Histogram
# Asked in:  
# Google
# Facebook
# Amazon
# Given an array of integers A of size N. A represents a histogram i.e A[i] denotes height of
# the ith histogram’s bar. Width of each bar is 1.

# Largest Rectangle in Histogram: Example 1

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

# Largest Rectangle in Histogram: Example 2

# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# Find the area of largest rectangle in the histogram.



# Input Format

# The only argument given is the integer array A.
# Output Format

# Return the area of largest rectangle in the histogram.
# For Example

# Input 1:
#     A = [2, 1, 5, 6, 2, 3]
# Output 1:
#     10
#     Explanation 1:
#         The largest rectangle is shown in the shaded area, which has area = 10 unit.


class Solution:
    # @param A : list of integers
    # @return an integer
#    def largestRectangleArea(self, A):
    def largestRectangleArea(self, A):
        stack, ans = list(), 0

        for i in range(len(A)):
            if not len(stack) or A[stack[-1]] <= A[i]:
                stack.append(i)
            else:
                while len(stack) and A[stack[-1]] >= A[i]:
                    idx = stack.pop()
                    area = (i - (stack[-1] + 1 if len(stack) else 0)) * A[idx]
                    ans = max(ans, area)
                stack.append(i)

        while len(stack):
            idx = stack.pop()
            area = (len(A) - (stack[-1] + 1 if len(stack) else 0)) * A[idx]
            ans = max(ans, area)

        return ans
