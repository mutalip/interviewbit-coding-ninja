# Best Time to Buy and Sell Stocks I
# Asked in:  
# Amazon
# Facebook
# Problem Description
# <div id=problem_description_markdown_content_value style=”background-color: #f9f9f9; padding: 5px 10px; “>Say you have an array, A, for which the ith element is the price of a given stock on day i.<p></p>

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Return the maximum possible profit.

# </div>

# Problem Constraints
# <div id=problem_constraints_markdown_content_value style=”background-color: #f9f9f9; padding: 5px 10px; “>0 <= len(A) <= 7e5<p></p>

# 1 <= A[i] <= 1e7

# </div>

# Input Format
# <div id=input_format_markdown_content_value style=”background-color: #f9f9f9; padding: 5px 10px; “>The first and the only argument is an array of integers, A.</div>

# Output Format
# <div id=output_format_markdown_content_value style=”background-color: #f9f9f9; padding: 5px 10px; “>Return an integer, representing the maximum possible profit.</div>

# Example Input
# <div id=example_input_markdown_content_value style=”background-color: #f9f9f9; padding: 5px 10px; “>Input 1:<p></p>

# A = [1, 2]
# Input 2:

# A = [1, 4, 5, 2, 4]
# </div>

# Example Output
# <div id=example_output_markdown_content_value style=”background-color: #f9f9f9; padding: 5px 10px; “>Output 1:<p></p>

# 1
# Output 2:

# 4
# </div>

# Example Explanation
# <div id=example_explanation_markdown_content_value style=”background-color: #f9f9f9; padding: 5px 10px; “>Explanation 1:<p></p>

# Buy the stock on day 0, and sell it on day 1.
# Explanation 2:

# Buy the stock on day 0, and sell it on day 2.
# </div>


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A)==0:
            return 0
        if len(A)==1:
            return 0
        temp=[]
        for i in range(0,len(A)-1):
            temp.append(A[i+1]-A[i])
        temp.sort()
        if temp[-1]<0:
            return 0
        
        return temp[-1]
        
        
