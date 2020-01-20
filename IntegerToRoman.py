# Integer To Roman
# Asked in:  
# Amazon
# Facebook
# Microsoft
# Twitter
# Please Note:
# Another question which belongs to the category of questions which are intentionally stated vaguely.
# Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.

# Given an integer A, convert it to a roman numeral, and return a string corresponding to its roman numeral version

#  Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all the needed clarifications and see the expected response using “See Expected Output” For the purpose of this question, https://projecteuler.net/about=roman_numerals has very detailed explanations. 


# Input Format

# The only argument given is integer A.
# Output Format

# Return a string denoting roman numeral version of A.
# Constraints

# 1 <= A <= 3999
# For Example

# Input 1:
#     A = 5
# Output 1:
#     "V"

# Input 2:
#     A = 14
# Output 2:
#     "XIV"

class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        mapper = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        ans = ''

        for ara, rom in mapper:
            cnt = A // ara
            ans += rom * cnt
            A -= cnt * ara
            if not A:
                break

        return ans
