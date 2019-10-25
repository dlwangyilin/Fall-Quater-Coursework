import SLL

def matrix_to_list(matrix):
    """
    Convert from an adjacency matrix to adjacency lists
    :param matrix: Input adjacency matrix[][]
    :return: Output a list of linked list, each linked list store the neighbours
    """
    length = len(matrix)
    lst = [SLL.LinkedList() for _ in range(length)]
    for i in range(length):
        for j in range(length):
            if matrix[i][j] == 1:
                lst[i].append(j)
    return lst

def list_to_incidence_matrix(list):
    """
    Convert from an adjacency list to an incidence matrix.An incidence matrix M has a row for each vertex and
    a column for each edge, such that M[i, j] = 1 if vertex i is part of edge j, otherwise M[i, j] = 0.
    :param list: A list of linked list
    :return: incidence matrix[][]
    """
    edge_num = 0
    for sll in list:
        edge_num += sll.getsize()
    edge_num = edge_num//2
    node_num = len(list)
    inc_matrix = [edge_num * [0] for _ in range(0, node_num)]
    edge_index_map = {}
    for node_index in range(0, node_num):
        for neighbor_index in list[node_index].iter():
            edge = tuple(sorted([node_index, neighbor_index]))
            if edge not in edge_index_map:
                edge_index_map[edge] = len(edge_index_map)
            edge_index = edge_index_map[edge]
            inc_matrix[node_index][edge_index] = 1
    return (inc_matrix,edge_index_map)

def incidence_matrix_to_list(incimatrix):
    """
    Convert from an incidence matrix to adjacency lists.
    :param incimatrix: Input incidence matrix[nodeindex][edgeindex]
    :param edgemap: dictionary{(edge):edgeindex}
    :return: adjacent linked list
    """
    nodenum = len(incimatrix)
    edgenum = len(incimatrix[0])
    # # switch map to index:tuple
    # reversemap = {}
    # for key, value in edgemap.items():
    #     reversemap[value] = key
    lst = [SLL.LinkedList() for _ in range(nodenum)]
    for edge_index in range(edgenum):
        temppair = []
        for node_index in range(nodenum):
            if incimatrix[node_index][edge_index] == 1:
                temppair.append(node_index)
        lst[temppair[0]].append(temppair[1])
        lst[temppair[1]].append(temppair[0])
    # for node_index in range(nodenum):
    #     for edge_index in range(edgenum):
    #         if incimatrix[node_index][edge_index] == 1:
    #             edge = reversemap[edge_index]
    #             node = edge[0] if node_index != edge[0] else edge[1]
    #             lst[node_index].append(node)
    return lst


if __name__ == '__main__':
    # All indices stored in adjacent list are started from zero,
    # and when print in main(), program will +1 for readable.
    # Question 1 - Convert from an adjacency matrix to adjacency lists
    print("---------from an adjacency matrix to adjacency lists----------")
    matrix = [[0,1,0,0,1],
              [1,0,1,1,1],
              [0,1,0,1,0],
              [0,1,1,0,1],
              [1,1,0,1,0]]
    lst = matrix_to_list(matrix)
    for i in range(len(matrix)):
        print(i + 1, end="")
        for data in lst[i].iter():
            print("->", data+1,end="")
        print("")

    # Question 2 - Convert from an adjacency list to an incidence matrix.
    print("---------from an adjacency list to incidence matrix----------")
    incimatrix = list_to_incidence_matrix(lst)[0]
    print(incimatrix)
    # edgemap = list_to_incidence_matrix(lst)[1]
    # print(edgemap)

    # Question 3 - Convert from an incidence matrix to adjacency lists.
    """
    incidence matrix:
    [[1, 1, 0, 0, 0, 0, 0],
     [1, 0, 1, 1, 1, 0, 0],
     [0, 0, 1, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 1, 1],
     [0, 1, 0, 0, 1, 0, 1]]

     edge map:
     {(0, 1): 0, (0, 4): 1, (1, 2): 2, (1, 3): 3, (1, 4): 4, (2, 3): 5, (3, 4): 6}
    """
    print("---------from an incidence matrix to adjacency lists----------")
    adjacency_lists = incidence_matrix_to_list(incimatrix)
    for i in range(len(adjacency_lists)):
        print(i + 1, end="")
        for data in adjacency_lists[i].iter():
            print("->", data+1,end="")
        print("")
