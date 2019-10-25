class Graph:
    def __init__(self, vertices, directed=False):
        self.__V = vertices
        self.__graph = [[0]*self.__V for _ in range(self.__V)]
        self.__directed = directed

        # Function to add an edge in an undirected graph

    def add_edge(self, u, v):
        # Adding the node to the source node
        self.__graph[u][v] = 1
        if not self.__directed:
            self.__graph[v][u] = 1

        # Function to print the graph

    def printgraph(self):
        print (self.__graph)

    def BFS(self, source):
        """
        BFS traversal
        :param source: source node
        :return: A list but used as queue
        """
        queue = []  # Store the order of upcoming visited node, FIFO
        marked = [False] * self.__V  # Store if the node is marked
        edgeTo = [0] * self.__V  # Store where is the current node from
        distTo = [0] * self.__V  # Store the shortest distance to the source
        queue.append(source)
        marked[source] = True
        edgeTo[source] = -1  # represent root
        distTo[source] = 0
        while queue:
            current = queue.pop(0)  # Always visit the first of queue
            print(chr(current+65), end="->")    # print char
            row = self.__graph[current]
            neighbors = []
            for j in range(self.__V):
                if row[j] == 1:
                    neighbors.append(j)
            for neighbor in neighbors:
                if marked[neighbor] is False:
                    queue.append(neighbor)
                    marked[neighbor] = True
                    edgeTo[neighbor] = current
                    distTo[neighbor] = distTo[current] + 1

    def DFS_preorder(self, source):
        def helper(current, marked, edgeTo):
            # Mark the current node as visited and print it
            marked[current] = True
            print(chr(current+65), end="->")

            row = self.__graph[current]
            neighbors = []
            for j in range(self.__V):
                if row[j] == 1:
                    neighbors.append(j)
            for neighbor in neighbors:
                if marked[neighbor] == False:
                    edgeTo[neighbor] = current
                    helper(neighbor, marked, edgeTo)

        marked = [False] * (self.__V)    # Store if the node is marked
        edgeTo = [0] * self.__V  # Store where is the current node from
        edgeTo[0] = -1
        helper(source, marked, edgeTo)



if __name__ == "__main__":
    g = Graph(10)
    """
    adjacency matrix =
    [[0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
     [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
     [1, 1, 0, 0, 1, 0, 1, 0, 0, 0],
     [0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]]

    """
    g.add_edge(0,1)    # (A,B)  - also g.add_edge(ord('A')-65, XXXXX)
    g.add_edge(0,3)    # (A,D)
    g.add_edge(0,8)    # (A,I)
    g.add_edge(1,2)    # (B,C)
    g.add_edge(1,3)    # (B,D)
    g.add_edge(1,4)    # (B,E)
    g.add_edge(2,4)    # (C,E)
    g.add_edge(2,5)    # (C,F)
    g.add_edge(3,4)    # (D,E)
    g.add_edge(3,6)    # (D,G)
    g.add_edge(4,5)    # (E,F)
    g.add_edge(4,6)    # (E,G)
    g.add_edge(4,7)    # (E,H)
    g.add_edge(5,7)    # (F,H)
    g.add_edge(6,7)    # (G,H)
    g.add_edge(6,8)    # (G,I)
    g.add_edge(6,9)    # (G,J)
    g.add_edge(7,9)    # (H,J)
    g.add_edge(8,9)    # (I,J)
    print("BFS is")
    g.BFS(0)
    print("")
    print("DFS preorder is")
    g.DFS_preorder(0)

