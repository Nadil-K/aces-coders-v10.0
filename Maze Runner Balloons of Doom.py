# Maze Runner: Balloons of Doom

class TreeNode:
    def __init__(self, color):
        self.color = color
        self.children = []
        self.parent = None
        self.blue_count_to_root = color

def construct_tree(structure, colors):
    tree_nodes = [TreeNode(colors[i]) for i in range(len(colors))]
    for i, parent in enumerate(structure):
        tree_nodes[parent - 1].children.append(tree_nodes[i + 1])
        tree_nodes[i + 1].parent = tree_nodes[parent - 1]
        tree_nodes[i + 1].blue_count_to_root = tree_nodes[parent - 1].blue_count_to_root + tree_nodes[i + 1].color
    return tree_nodes

def get_lca(node1, node2):
    ancestors_node1 = set()
    while node1:
        ancestors_node1.add(node1)
        node1 = node1.parent

    while node2:
        if node2 in ancestors_node1:
            return node2
        node2 = node2.parent

def calculate_color_sum(node1, node2):
    lca_node = get_lca(node1, node2)
   
    color_sum_node1 = 0
    while node1 != lca_node:
        color_sum_node1 += node1.color
        node1 = node1.parent

    color_sum_node2 = 0
    while node2 != lca_node:
        color_sum_node2 += node2.color
        node2 = node2.parent

    return color_sum_node1 + color_sum_node2 + lca_node.color

n, q = map(int, input().split())
colors = list(map(int, input().split()))
structure = list(map(int, input().split()))

tree_nodes = construct_tree(structure, colors)

for _ in range(q):
    node1_index, node2_index = map(int, input().split())
    print(calculate_color_sum(tree_nodes[node1_index-1], tree_nodes[node2_index-1]))

