# Largest Number
# Asked in:  
# Amazon
# Goldman Sachs
# Microsoft
# Given a list of non negative integers, arrange them such that they form the largest number.

# For example:

# Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.

from functools import cmp_to_key
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = map(str, A)
        key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
        res = ''.join(sorted(A, key= key, reverse=True))
        # Must left trim 0, apparently
        res = res.lstrip('0')
        return res if res else '0'
