# NoodleCable Network Troubleshooting

from collections import defaultdict
import math

def compute_ancestors_table(node_parents, max_depth):
    node_ancestors = defaultdict(lambda: [-1] * (max_depth + 1))
    
    for node, parent in node_parents.items():
        node_ancestors[node][0] = parent
    
    for depth in range(1, max_depth + 1):
        for node in node_parents.keys():
            if node_ancestors[node][depth-1] != -1:
                node_ancestors[node][depth] = node_ancestors[node_ancestors[node][depth-1]][depth-1]
    return node_ancestors

def get_ancestor_at_distance(node, distance, node_ancestors, max_depth):
    for depth in range(max_depth, -1, -1):
        if node == -1:
            return "None"
        if distance >= (1 << depth):
            node = node_ancestors[node][depth]
            distance -= (1 << depth)
    return node if node != -1 else "None"

num_nodes = int(input())
node_parents = defaultdict(lambda: -1)
max_depth = math.ceil(math.log2(num_nodes))

for _ in range(num_nodes):
    child_node, parent_node = input().split()
    node_parents[child_node] = parent_node if parent_node != "ROOT" else -1

node_ancestors_table = compute_ancestors_table(node_parents, max_depth)

num_queries = int(input())
for _ in range(num_queries):
    query_components = input().split()
    operation = query_components[0]

    if operation == 'N':
        _, parent, child = query_components
        node_parents[child] = parent
        node_ancestors_table[child] = [-1] * (max_depth + 1)
        node_ancestors_table[child][0] = parent
        for depth in range(1, max_depth + 1):
            if node_ancestors_table[child][depth-1] != -1:
                node_ancestors_table[child][depth] = node_ancestors_table[node_ancestors_table[child][depth-1]][depth-1]

    elif operation == 'R':
        _, node_to_remove = query_components
        node_parents[node_to_remove] = -1
        node_ancestors_table[node_to_remove] = [-1] * (max_depth + 1)

    elif operation == 'F':
        _, target_node, distance = query_components
        distance = int(distance)
        print(get_ancestor_at_distance(target_node, distance, node_ancestors_table, max_depth))