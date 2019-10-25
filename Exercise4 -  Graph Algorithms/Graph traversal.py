from collections import defaultdict
class Graph:
    def __init__(self, directed = False):
        """
        Graph is stored as dict
        """
        self.__graph = defaultdict(list)    #if key doesn't exist, return an empty list
        self.__directed = directed

    def addEdge(self, node, neighbor):
        """
        add a edge to the graph. graph is a dict{}. key is node, value is a list of neighbor.
        :param node:
        :param neighbor:
        :return:
        """
        self.__graph[node].append(neighbor)
        if not self.__directed:
            self.__graph[neighbor].append(node)

    def BFS(self, source):
        """
        BFS traversal
        :param source: source node
        :return: A list but used as queue
        """
        queue = []  # Store the order of upcoming visited node, FIFO
        marked = [False]*len(self.__graph)    # Store if the node is marked
        edgeTo = [0]*len(self.__graph)    # Store where is the current node from
        distTo = [0]*len(self.__graph)    # Store the shortest distance to the source
        queue.append(source)
        marked[source] = True
        edgeTo[source] = -1 # represent root
        distTo[source] = 0
        while queue:
            current = queue.pop(0)    # Always visit the first of queue
            print(current, end="->")
            neighbors = self.__graph[current]
            neighbors.sort()
            for neighbor in neighbors:
                if marked[neighbor] is False:
                    queue.append(neighbor)
                    marked[neighbor] = True
                    edgeTo[neighbor] = current
                    distTo[neighbor] = distTo[current] + 1

    def DFS(self, source):
        def helper(current, marked):
            # Mark the current node as visited
            # and print it
            marked[current] = True
            print(current, end='->')

            # Recur for all the vertices
            # adjacent to this vertex
            for i in sorted(self.__graph[current]):
                if marked[i] == False:
                    helper(i, marked)

        marked = [False] * (len(self.__graph))
        helper(source, marked)

g = Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,0)

g.BFS(0)
g.DFS(0)