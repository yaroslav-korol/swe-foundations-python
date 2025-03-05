    ### ADJACENCY LIST ###
# adjacency_list = {
#     'a': ['b', 'c'],
#     'b': ['d'],
#     'c': ['e'],
#     'd': ['f'],
#     'e': [],
#     'f': []
# }



# adjacency_list = {
#     '0': ['1'],
#     '1': ['4'],
#     '2': [],
#     '3': ['5'],
#     '4': ['2', '3'],
#     '5': []
# }


    ### DEPTH FIRST TRAVERSAL. EXPLICIT (ITERATION) WAY  ###
# def dep_first_print(graph, src):
#     stack = [src]

#     while len(stack) > 0:
#         current = stack.pop()
#         print(current)
#         for neighbor in graph[current]:
#             stack.append(neighbor)

# source = 'a'
# dep_first_print(adjacency_list, source)



    ### DEPTH FIRST TRAVERSAL. RECURSION WAY  ###
# def dep_first_print(graph, src):
#     print(src)
#     for neighbor in graph[src]:
#         dep_first_print(graph, neighbor)

# source = '1'
# dep_first_print(adjacency_list, source)


    ### BREADTH FIRST TRAVERSAL ###
# Because this method uses queue, we can't use recursion way for BFT (recursion use stack)

# def breadth_first_print(graph, src):
#     queue = [src]

#     while len(queue) > 0:
#         current = queue.pop(0)
#         print(current)
#         for neighbor in graph[current]:
#             queue.append(neighbor)

# source = 'a'
# breadth_first_print(adjacency_list, source)




    ### EXERCISES ###

# HAS PATH #

# DFT Recursive Solution #

# def has_path(graph, src, dst):
#   if src == dst:
#     return True
#   for neighbor in graph[src]:
#     if has_path(graph, neighbor, dst):
#       return True
#   return False

# source = '1'
# answer = has_path(adjacency_list, source, '5')
# print(answer)

# BFT Iterative Solution #

# def has_path(graph, src, dst):
#   queue = [src]
#   while len(queue) > 0:
#     current = queue.pop(0)
#     if current == dst: return True
#     for neighbor in graph[current]:
#       queue.append(neighbor)
#   return False




# UNDIRECTED PATH #

# def undirected_path(edges, node_a, node_b):
#     # graph = build_graph(edges)
#     graph = edges
#     return has_path(graph, node_a, node_b, set())



# def has_path(graph, src, dst, visited):
#     if src == dst:
#         return True
#     # Check visited Nodes to avoid cycles (infinite loops)
#     if src in visited:
#         return False
#     # Create list to track visited nodes
#     # visited.append(src)
#     visited.add(src)
#     # Check every neighbor of source recursively
#     for neighbor in graph[src]:
#         if has_path(graph, neighbor, dst, visited):
#             return True
#     return False



# def build_graph(edges):
#     graph = {}

#     for edge in edges:
#         [a, b] = edge
#         if not a in graph: graph[a] = []
#         if not b in graph: graph[b] = []
#         graph[a].append(b)
#         graph[b].append(a)
#     return graph

# graph_edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]

# graph = build_graph(graph_edges)
# answer = undirected_path(graph_edges, 'j', 'm')
# print(answer)


print(True or False)