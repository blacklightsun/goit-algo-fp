import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def add_nodes(center_node, heap, i):
    # мій код - рекурсивна функція для створення дерева з купи, як списку значень
    if 2 * i + 1 < len(heap):
        left_node = Node(heap[2 * i + 1])
        center_node.left = left_node
        add_nodes(left_node, heap, 2 * i + 1)

    if 2 * i + 2 < len(heap):
        right_node = Node(heap[2 * i + 2])
        center_node.right = right_node
        add_nodes(right_node, heap, 2 * i + 2)

# Створення купи
heap = [10, 3, 4, 5, 17, 8, 2, 1, 15, 16, 14, 11]
heapq.heapify(heap)

# Створення дерева
if len(heap) >= 1:
    start_node = Node(heap[0])
    add_nodes(start_node, heap, 0)

    # Відображення дерева
    print(f'Купа у вигляді списку: {heap}')
    draw_tree(start_node)
else:
    print('У купі немає елементів для побудови графа')
