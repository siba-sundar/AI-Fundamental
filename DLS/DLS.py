adj_list = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['e'],
    'd': ['e', 'f'],
    'e': ['f'],
    'f': []
}


def dfs_iterative(adj_list, source, level_limit):
    stack = [(source, 0)]
    visited = set()
    result = []

    while stack:
        node, current_level = stack.pop()

        if node in visited or current_level > level_limit:
            continue

        visited.add(node)
        result.append(node)


        for next in adj_list[node]:
            stack.append((next, current_level + 1))  # Add at the end of the stack



    return result



source = 'a'
level_limit = 2


result_nodes = dfs_iterative(adj_list, source, level_limit)


print("Nodes reachable within", level_limit, "levels:", result_nodes)
