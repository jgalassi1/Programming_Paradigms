def tree_to_text(tree, root_node):
    # text to keep track of in order notation
    text = ""
    # push root_node to stack
    stack = [root_node]
    while stack:
        current_node = stack[len(stack)-1]
        if tree[current_node]:
            current_node = tree[current_node][0]
            stack.append(current_node)
        else:
            text += stack.pop(len(stack)-1).split("_",1)[1]
            if stack:
                current_node = stack.pop(len(stack)-1)
                text += current_node.split("_",1)[1]
                current_node = tree[current_node][1]
                stack.append(current_node)
    return text
