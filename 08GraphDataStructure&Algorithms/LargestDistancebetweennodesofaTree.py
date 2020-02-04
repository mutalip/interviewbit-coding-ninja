# Largest Distance between nodes of a Tree
# Asked in:  
# Facebook
# Google
# Problem Setter: ulugbek_adilbekov Problem Tester: raghav_aggiwal
# Find largest distance
# Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000) nodes. The goal of the problem is to find largest distance between two nodes in a tree. Distance between two nodes is a number of edges on a path between the nodes (there will be a unique path between any pair of nodes since it is a tree). The nodes will be numbered 0 through N - 1.

# The tree is given as an array P, there is an edge between nodes P[i] and i (0 <= i < N). Exactly one of the i’s will have P[i] equal to -1, it will be root node.

#  Example:
# If given P is [-1, 0, 0, 0, 3], then node 0 is the root and the whole tree looks like this: 
#           0
#        /  |  \
#       1   2   3
#                \
#                 4  
#  One of the longest path is 1 -> 0 -> 3 -> 4 and its length is 3, thus the answer is 3. Note that there are other paths with maximal distance".
# 
 import heapq
import resource
import sys

# Will segfault without this line.
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        children = {}
        root = None
        for i, x in enumerate(A):
            if x == -1:
                root = i
            else:
                if x in children:
                    children[x] += [i]
                else:
                    children[x] = [i]

        largest_dist = 0

        for k,v in self.dfs(root, children, 0, {}).items():
            largest_dist = max(self.largest_dist_from_paths(v), largest_dist)

        return largest_dist

    def largest_dist_from_paths(self, paths):
        paths += [0, 0]
        a, b = heapq.heappop(paths), heapq.heappop(paths)
        return -1 * (a + b)

    def dfs(self, root, children, path_len, paths):
        paths[root] = [0]

        if root not in children: return paths

        for child in children[root]:
            paths = self.dfs(child, children, path_len + 1, paths)
            heapq.heappush(paths[root], min(paths[child]) - 1)

        return paths
