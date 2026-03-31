def dfs(undirected_adj_matrix, node_label):
    """
    Implementing Depth First Search Algorithm to gain a better understanding of graphs
    Args: undirected_adj_matrix: Access row in the matrix
          node_label: numeric value of the node between 0 and n-1, where n is the total number of nodes in the graph
    Return: visited
    """
    
    stack = [node_label]
    visited = []
    
    while stack:
        node = stack.pop() # pop node from last element in the list since dfs is FIFO
        
        if node not in visited:
            visited.append(node) # add node to visited

            # Add all univisted neighbors to stack
            for index, value in enumerate(undirected_adj_matrix[node]):
                if value == 1:
                    stack.append(index)
                    
    return visited

# --> Example usage <--
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3))
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))
print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3))
print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0))