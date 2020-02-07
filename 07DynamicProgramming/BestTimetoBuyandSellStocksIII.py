# Best Time to Buy and Sell Stocks III
# Asked in:  
# Amazon
# Facebook
# Say you have an array, A, for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most 2 transactions.

# Return the maximum possible profit.

# Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


# Input Format:

# The first and the only argument is an integer array, A.
# Output Format:

# Return an integer, representing the maximum possible profit.
# Constraints:

# 1 <= length(A) <= 7e5
# 1 <= A[i] <= 1e7
# Examples:

# Input 1:
#     A = [1, 2, 1, 2]

# Output 1:
#     2

# Explanation 1: 
#     Day 0 : Buy 
#     Day 1 : Sell
#     Day 2 : Buy
#     Day 3 : Sell

# Input 2:
#     A = [7, 2, 4, 8, 7]

# Output 2:
#     6

# Explanation 2:
#     Day 1 : Buy
#     Day 3 : Sell

#class Solution:
    # @param A : tuple of integers
    # @return an integer
#    def maxProfit(self, A):
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        buy1, sell1 = -float('INF'), 0
        buy2, sell2 = -float('INF'), 0

        for a in A:
            sell2 = max(sell2, a + buy2)
            buy2 = max(buy2, sell1 - a)
            sell1 = max(sell1, a + buy1)
            buy1 = max(buy1, -a)

        return sell2
