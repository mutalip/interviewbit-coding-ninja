# Pretty Json
# Asked in:  
# Facebook
# Microsoft
# Given a string A representating json object. Return an array of string denoting json object with proper indentaion.

# Rules for proper indentaion:

# Every inner brace should increase one indentation to the following lines.
# Every close brace should decrease one indentation to the same line and the following lines.
# The indents can be increased with an additional ‘\t’
# Note:

# [] and {} are only acceptable braces in this case.

# Assume for this problem that space characters can be done away with.



# Input Format

# The only argument given is the integer array A.
# Output Format

# Return a list of strings, where each entry corresponds to a single line. The strings should not have "\n" character in them.
# For Example

# Input 1:
#     A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"
# Output 1:
#     { 
#         A:"B",
#         C: 
#         { 
#             D:"E",
#             F: 
#             { 
#                 G:"H",
#                 I:"J"
#             } 
#         } 
#     }

# Input 2:
#     A = ["foo", {"bar":["baz",null,1.0,2]}]
# Output 2:
#    [
#         "foo", 
#         {
#             "bar":
#             [
#                 "baz", 
#                 null, 
#                 1.0, 
#                 2
#             ]
#         }
#     ]



class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        indent = 0
        res = []
        line = ''
        for x in A:
            if x in '{[':
                if line:
                    res.append(line)
                res.append('\t' * indent + x)
                line = ''
                indent += 1
            elif x in ']}':
                if line:
                    res.append(line)
                indent -= 1
                line = '\t' * indent + x  # Might be followed by ','
            else:
                if not line:
                    line = '\t' * indent
                line += x
                if x == ",":
                    res.append(line)
                    line = ''
        if line:
            res.append(line)
        return res
