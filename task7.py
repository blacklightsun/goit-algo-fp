import numpy as np

# кількість випробувань
experiment_qty = 100000

probability_result_dict = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}

result_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

for throw in range(experiment_qty):
    cube1 = np.random.randint(1, 7)
    cube2 = np.random.randint(1, 7)
    throw_sum = cube1 + cube2
    result_dict[throw_sum] += 1 / experiment_qty

print('\nВизначення ймовірності методом Монте-Карло')
for i in range(2, 13):
    print(f'сума: {i:2d}, теоретична ймовірність: {round(probability_result_dict[i] * 100, 2):5.2f}%, практична ймовірність за методом Монте-Карло: {round(result_dict[i] * 100, 2):5.2f}%, відхилення: {round((result_dict[i] / probability_result_dict[i] - 1) * 100, 2):6.2f}%')

