# Roman To Integer
# Asked in:  
# Amazon
# Facebook
# Microsoft
# Twitter
# Given a string A representing a roman numeral.
# Convert A into integer.

# A is guaranteed to be within the range from 1 to 3999.

# NOTE: Read more
# details about roman numerals at Roman Numeric System



# Input Format

# The only argument given is string A.
# Output Format

# Return an integer which is the integer verison of roman numeral string.
# For Example

# Input 1:
#     A = "XIV"
# Output 1:
#     14

# Input 2:
#     A = "XX"
# Output 2:
#     20

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        roman = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        # The last letter always gets added
        _sum = roman[A[-1]]
        # Iterate over A in pairs of two
        for x, y in zip(A[:-1], A[1:]):
            current, _next = roman[x], roman[y]
            # If pair is like IV
            if current < _next:
                _sum -= current
            # Else if like VI
            else:
                _sum += current
        return _sum
        
