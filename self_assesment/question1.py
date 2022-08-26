def bfs_traversal(graph, initial_node):
    # queue for bfs traversal
    bfs_queue = []
    # list to keep track of order of bfs traversal
    bfs_list = []
    bfs_queue.append(initial_node)
    while bfs_queue:
        # pop from queue
        current_node = bfs_queue.pop(0)
        # add to queue
        bfs_list.append(current_node)
        # iterate through paths from node
        for node in graph[current_node]:
            if node not in bfs_list:
                bfs_queue.append(node)
    return bfs_list
