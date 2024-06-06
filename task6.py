class Food:
    # клас для жадібного алгоритма
    def __init__(self, name, cost, value):
        self.name = name
        self.cost = cost
        self.value = value
        self.ratio = value / cost


def greedy_algorithm(food_items: dict, budget: int) -> int:

    # підготовка даних
    food_specs_list = [Food(i[0], i[1]['cost'], i[1]['calories']) for i in food_items.items()]

    # сортування по калорійності на одну грошову одиницю
    food_specs_list.sort(key=lambda x: x.ratio, reverse=True)

    # цикл розрахунку
    total_value = 0
    total_cost = 0
    selected_food_list = []
    print("\nКалорійність на 1-ну грошову одиницю (довідково):")
    for food in food_specs_list:
        print(f'{food.name:9s}: {round(food.ratio, 1):4.1f} кКал/$')  # довідково
        if budget >= food.cost:
            budget -= food.cost
            total_value += food.value
            total_cost += food.cost
            selected_food_list.append(food.name)

    return total_cost, total_value, selected_food_list


def dynamic_programming(food_items, budget):

    # підготовка даних
    n = len(food_items)
    food_name = []
    food_cost = []
    food_calories = []
    for food in food_items.items():
        food_name.append(food[0])
        food_cost.append(food[1]['cost'])
        food_calories.append(food[1]['calories'])

    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    # створюємо таблицю menu для зберігання оптимальних значень харчів
    menu = [[[] for _ in range(budget + 1)] for _ in range(n + 1)]

    # будуємо таблиці K, menu знизу вгору
    for i in range(n + 1):
        for b in range(budget + 1):
            if i == 0 or b == 0:
                K[i][b] = 0
            elif food_cost[i - 1] <= b:
                K[i][b] = max(food_calories[i - 1] + K[i - 1][b - food_cost[i - 1]], K[i - 1][b])

                if food_calories[i - 1] + K[i - 1][b - food_cost[i - 1]] >= K[i - 1][b]:
                    menu[i][b].extend(menu[i - 1][b - food_cost[i - 1]])
                    menu[i][b].append(food_name[i - 1])
                else:
                    menu[i][b] = menu[i - 1][b]

            else:
                K[i][b] = K[i - 1][b]
                menu[i][b] = menu[i - 1][b]

    # розраховуємо вартість оптимального набору харчів
    total_cost = 0
    for food in menu[n][budget]:
        total_cost += food_items[food]['cost']

    return total_cost, K[n][budget], menu[n][budget]


# специфікація харчів
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
# бюджет на їжу
budget = 100

# розрахунок по двум алгоритмам
costs, values, food_list = greedy_algorithm(items, budget)
print(f'\nОптимальне меню за жадібним алгоритмом: {food_list}. Витрачено ${costs} при бюджеті в ${budget}, отримано {values} кКал.')

costs, values, food_list = dynamic_programming(items, budget)
print(f'\nОптимальне меню за алгоритмом динамічного програмування: {food_list}. Витрачено ${costs} при бюджеті в ${budget}, отримано {values} кКал.')
