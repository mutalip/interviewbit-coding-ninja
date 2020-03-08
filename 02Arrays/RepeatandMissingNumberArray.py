# Repeat and Missing Number Array
# Asked in:  
# Amazon
# Please Note:
# There are certain problems which are asked in the interview to also check how you take care of overflows in your problem.
# This is one of those problems.
# Please take extra care to make sure that you are type-casting your ints to long properly and at all places. Try to verify if your solution works if number of elements is as large as 105

#  Food for thought :
# Even though it might not be required in this problem, in some cases, you might be required to order the operations cleverly so that the numbers do not overflow.
# For example, if you need to calculate n! / k! where n! is factorial(n), one approach is to calculate factorial(n), factorial(k) and then divide them.
# Another approach is to only multiple numbers from k + 1 ... n to calculate the result.
# Obviously approach 1 is more susceptible to overflows.

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        pow = lambda i: i * i

        # Sa = A1 + A2 + ... + An, Sn = 1 + 2 + ... + n
        Sa, Sn = sum(A), sum(range(1, len(A) + 1))

        # sqSa = A1^2 + A2^2 + ... + An^2, sqSn = 1^2 + 2^2 + ... + n^2
        sqSa, sqSn = sum(map(pow, A)), sum(map(pow, range(1, len(A) + 1)))

        c = Sn - Sa

        a = int(((sqSn - sqSa) / c - c) / 2)
        b = int(c + a)

        return a, b
