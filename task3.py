import networkx as nx
import heapq

# дані для побудови схеми (вихідний малюнок тут же у теці)
crossing_list = [
    ("Заводська", "Прутська"),
    ("Прутська", "Вокзальна"),
    ("Вокзальна", "Центральна"),
    ("Центральна", "Зелена"),
    ("Зелена", "Фастівська"),
    ("Фастівська", "Гравітон"),
    ("Московська", "Садгірська"),
    ("Садгірська", "Калинівський ринок"),
    ("Калинівський ринок", "Центральна"),
    ("Центральна", "Парк ім. Шевченка"),
    ("Парк ім. Шевченка", "Проспект Незалежності"),
    ("Проспект Незалежності", "Озерна"),
    ("Університет", "Вокзальна"),
    ("Вокзальна", "Калинівський ринок"),
    ("Калинівський ринок", "Фастівська"),
    ("Фастівська", "Аеропорт"),
    ("Аеропорт", "Проспект Незалежності"),
    ("Проспект Незалежності", "Дубинська"),
    ("Дубинська", "Горіхівська"),
    ("Горіхівська", "Цецино"),
    ("Цецино", "Університет"),
]
edge_lenght_list = [2.5, 7.0, 3.0, 1.5, 4.0,
                    2.0, 3.0, 5.0, 1.5, 2.0,
                    6.0, 1.0, 5.5, 3.0, 1.5,
                    1.0, 3.5, 5.0, 2.5, 4.5,
                    1.5]

# створюємо зважений граф
G = nx.Graph(crossing_list)
for i, edge in enumerate(crossing_list):
    G[edge[0]][edge[1]]['lenght'] = edge_lenght_list[i]

def dijkstra(graph, start_node):
    # функція написана по опису алгоритму з конспекту, без підглядання в код з конспекту
    # upd: вибір найближчої ноди реалізований за допомогою бінарної купи
    dist_dict = {node: float('inf') for node in graph.nodes}  # початковий словник відстаней
    dist_dict[start_node] = 0

    unvisited_heap = [(float('inf'), node) for node in graph.nodes]  # початкова купа невідвіданих нод
    heapq.heapify(unvisited_heap)  # з даними про відстань до них

    while unvisited_heap:
        for node in graph[start_node]:  # оновлення відстаней від поточної ноди
            if dist_dict[node] > dist_dict[start_node] + graph[start_node][node]['lenght']:
                dist_dict[node] = dist_dict[start_node] + graph[start_node][node]['lenght']

        i_for_pop = None
        for i in range(len(unvisited_heap)):
            unvisited_heap[i] = (dist_dict[unvisited_heap[i][1]], unvisited_heap[i][1])  # сінхронизація купи та словника відстаней
            if unvisited_heap[i][1] == start_node:  # пошук індексу відвіданої ноди для видалення її з купи
                i_for_pop = i

        if i_for_pop:
            unvisited_heap.pop(i_for_pop)  # видалення відвіданої ноди
        heapq.heapify(unvisited_heap)  # перебудова купи після видалення відвіданої ноди

        # пошук найближчої ноди для переходу
        start_node = heapq.heappop(unvisited_heap)[1]

    return dist_dict

start = "Центральна"
print(f'\nНайкоротші дистанції від станції {start}:')
for node, dist in dijkstra(G, start).items():
    print(node, dist)