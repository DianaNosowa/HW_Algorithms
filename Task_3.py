class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        number_of_node = len(isConnected) # city number
        visited = [False] * number_of_node # list of visited nodes
        province = 0 # province counter
        for i in range(number_of_node): 
            if not visited[i]:
                province += 1 # found a new province
                self.dfs(isConnected, visited, i)
        return province

    def dfs(self, isConnected, visited, node):
        visited[node] = True  # mark current city as visited
        n = len(isConnected)
        for neighbor in range(n): # go through all neighbors
            if isConnected[node][neighbor] == 1 and not visited[neighbor]: # if connected and not visited yet, explore it
                self.dfs(isConnected, visited, neighbor)
