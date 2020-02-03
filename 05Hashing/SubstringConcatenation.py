# Substring Concatenation
# Asked in:  
# Facebook
# You are given a string, S, and a list of words, L, that are all of the same length.

# Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

# Example :

# S: "barfoothefoobarman"
# L: ["foo", "bar"]
# You should return the indices: [0,9].
# (order does not matter).
class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    #def findSubstring(self, A, B):
    def findSubstring(self, A, B):
        lits_size=len(B)
        word_size=len(B[0])
        i=0
        ans=[]
        comp=0
        for word in B:
            comp+=hash(word)
        while (i+(lits_size)*(word_size)<=len(A)):
            x=list(A[i:i+(lits_size)*(word_size)])
            j=-1
            temp=[]
            final=0
            while x!=[]:
                k=0
                tempword=[]
                while k<word_size:
                    y=x.pop(0)
                    tempword.append(y)
                    k+=1
                temp.append("".join(tempword))
                final+=hash("".join(tempword))
            if comp==final:
                ans.append(i)
            i+=1
        return ans
