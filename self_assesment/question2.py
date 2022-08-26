def dfs_traversal(graph, initial_node):
    # function to perform dfs recursively
    def dfs_recursion(graph, current_node, dfs_list):
        # return if node has been already reached
        if current_node in dfs_list:
            return
        # append to list if node hasn't been reached
        dfs_list.append(current_node)
        # recursively go through each path of the node
        for node in graph[current_node]:
            dfs_recursion(graph, node, dfs_list)
    # list to keep track of what has been reached and in what order
    dfs_list = []
    # call recursive function
    dfs_recursion(graph, initial_node, dfs_list)
    return dfs_list