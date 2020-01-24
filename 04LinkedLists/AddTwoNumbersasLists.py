# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

#     342 + 465 = 807
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        ## The way we will be doing this will be by adding as we move
        ## through the lists. The answer already gave us the list
        ## numbers reversed for this very reason.
        
        ## We do the first instance of the sum outside of the loop as it
        ## will be our root.
        currSum = A.val + B.val
        
        ## Adding a number mod 10 is the same of adding a number base 10
        ## so if we get 16, for example, we will only put 6 in the node
        root = ListNode(currSum % 10)
        curr = root
        
        ## This is true division, so as in the last example, 16 // 10 is 1
        remainder = currSum // 10

        ## And then we move forward with the list.
        A = A.next
        B = B.next
        
        ## We add a 'last' variable for the ending in zero edge case
        ## i.e.: 0 -> 7 -> 9 -> 0
        last = None
        
        ## These three whiles will make sure we move through the lists
        ## properly, since they aren't guaranteed to be the same size
        ## In another language, we could use a "switch" statement, but
        ## python doesn't have those.
        while A is not None and B is not None:
            currSum = A.val + B.val + remainder
            remainder = currSum // 10
            curr.next = ListNode(currSum % 10)
            A = A.next
            B = B.next
            last = curr
            curr = curr.next
        while A is not None and B is None:
            currSum = A.val + remainder
            remainder = currSum // 10
            curr.next = ListNode(currSum % 10)
            A = A.next
            last = curr
            curr = curr.next
        while A is None and B is not None:
            currSum = B.val + remainder
            remainder = currSum // 10
            curr.next = ListNode(currSum % 10)
            B = B.next
            last = curr
            curr = curr.next
            
        ## We check if there is any remainder pending. If there
        ## is, we add it. This will happen at most once, so we
        ## only need an if to check this.
        if remainder != 0:
            currSum = remainder
            remainder = 0
            curr.next = ListNode(currSum % 10)
            curr = curr.next
        
        ## We know check the edge case mentioned in the problem,
        ## and if we find a 0 in the last instance we delete it
        ## by removing the reference to it from the list.
        if curr.val == 0:
            last.next = None
        
        return root
