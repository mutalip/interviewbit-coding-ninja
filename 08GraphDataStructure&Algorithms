# Clone Graph
# Asked in:  
# Google
# Facebook
# Amazon
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

#class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
#    def cloneGraph(self, node):
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    # def _cloneGraph(self, node, dp):
    #     if node == None:
    #         return None

    #     if node.label in dp:
    #         return dp[node.label]

    #     cloned = UndirectedGraphNode(node.label)
    #     dp[cloned.label] = cloned

    #     for neighbor in node.neighbors:
    #         cloned.neighbors.append(self._cloneGraph(neighbor, dp))

    #     return cloned

    # def cloneGraph(self, node):
    #     if node == None:
    #         return None
    #     dp = dict()
    #     return self._cloneGraph(node, dp)  
    def __init__(self):
        self.visited = {}
    
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node not in self.visited:
            new_node = UndirectedGraphNode(node.label)
            self.visited[node] = new_node
            new_node.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]
        return self.visited[node]
