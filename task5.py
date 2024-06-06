import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    # код з умов завдання
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    # код з умов завдання
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
    # код з умов завдання, доданий тільки останній рядок, щоб поверталися дані з функції
    tree = nx.Graph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    # colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    # plt.figure(figsize=(8, 5))
    # nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    # plt.title('Test')
    # plt.show()
    return tree, pos, labels

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

def dfs_iterative(graph, start_vertex):
    # мій код - ітеративний обхід графа в глибину
    visited = set()
    path_list = []
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        if vertex not in visited:
            # print(vertex, end=' ')
            # Відвідуємо вершину
            path_list.append(vertex)
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(list(graph[vertex].keys())))
    return path_list

def bfs_iterative(graph, start):
    # мій код - ітеративний обхід графа в ширину
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    path_list = []
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            # print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            path_list.append(vertex)
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(list(graph[vertex].keys())) - visited)
    # Повертаємо список відвіданих вершин після завершення обходу
    return path_list


# далі мій код ##########################

# Створення купи
heap = [10, 3, 4, 5, 17, 8, 2, 1, 15, 16, 14, 11, 9, 12]
heapq.heapify(heap)

# Створення дерева
if len(heap) >= 1:
    start_node = Node(heap[0])
    add_nodes(start_node, heap, 0)

    # Відображення дерева
    print(f'Купа у вигляді списку: {heap}')
    graph, pos, labels = draw_tree(start_node)
else:
    print('У купі немає елементів для побудови графа')

input('Для візуалізації обходу бінарної купи в глибину натисність Enter')
dfs_path = dfs_iterative(graph, start_node.id)
for i in range(len(dfs_path)):
    colors = list(reversed(range(1, i + 2)))
    colors.extend([0 for _ in range(len(dfs_path) - i -1 )])
    # print(colors)
    plt.figure(figsize=(8, 5))
    nx.draw(graph,
            pos=pos,
            nodelist=dfs_path,
            labels=labels,
            arrows=False,
            node_size=2500,
            cmap=plt.cm.Blues,
            edgecolors='black',
            node_color=colors)
    plt.show()

input('Для візуалізації обходу бінарної купи в ширину натисність Enter')
bfs_path = bfs_iterative(graph, start_node.id)
for i in range(len(bfs_path)):
    colors = list(reversed(range(1, i + 2)))
    colors.extend([0 for _ in range(len(bfs_path) - i - 1)])
    plt.figure(figsize=(8, 5))
    nx.draw(graph,
            pos=pos,
            nodelist=bfs_path,
            labels=labels,
            arrows=False,
            node_size=2500,
            cmap=plt.cm.Blues,
            edgecolors='black',
            node_color=colors)
    plt.show()
