# Combination Sum
# Asked in:  
# Facebook
# Amazon
# Adobe
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

#  Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The combinations themselves must be sorted in ascending order.
# CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
# The solution set must not contain duplicate combinations.
# Example,
# Given candidate set 2,3,6,7 and target 7,
# A solution set is:

# [2, 2, 3]
# [7]
#  Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
# Example : itertools.combinations in python.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
#    def combinationSum(self, A, B):
    def combinationSum(self,arr,target):
        index, ans, temp = 0, set(), []
        self.combination(arr,index,target,ans,temp)
        ans = list(ans) #convert to list
        return sorted(ans)
    def combination(self,arr,index,target,ans,temp):
        temp_sum = sum(temp)
        if temp_sum == target:
            ans.add(tuple(sorted(temp[:])))# sort and only add non duplicate tuples
            return
        elif temp_sum > target:
            return
        else:
            for i in range(index,len(arr)):
                temp.append(arr[i])
                self.combination(arr,index,target,ans,temp)
                i+=1
                temp.pop()
