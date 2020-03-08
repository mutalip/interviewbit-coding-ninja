# Spiral Order Matrix II
# Asked in:  
# Microsoft
# JP Morgan
# Amazon
# Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.



# Input Format:

# The first and the only argument contains an integer, A.
# Output Format:

# Return a 2-d matrix of size A x A satisfying the spiral order.
# Constraints:

# 1 <= A <= 1000
# Examples:

# Input 1:
#     A = 3

# Output 1:
#     [   [ 1, 2, 3 ],
#         [ 8, 9, 4 ],
#         [ 7, 6, 5 ]   ]

# Input 2:
#     4

# Output 2:
#     [   [1, 2, 3, 4],
#         [12, 13, 14, 5],
#         [11, 16, 15, 6],
#         [10, 9, 8, 7]   ]


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        mat = [[0] * A for i in range(A)]
        steps, curr = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
        i = j = k = 0   # current position (i, j), and current ring k
        tmp = 1         # current element


        while tmp <= A * A:
            mat[i][j] = tmp
            tmp += 1
            step_x, step_y = steps[curr]
            i, j = i + step_x, j + step_y

            # check does current position match any corner or current ring (k)
            curr += (curr == 0 and j == A - 1 - k) + (curr == 1 and i == A - 1 - k) + (curr == 2 and j == k) + (curr == 3 and i == k)

            if curr == 4:
                i, j, k, curr = i + 1, j + 1, k + 1, 0

        return mat
