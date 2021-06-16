"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"Исходный массив: {array}")

min_item = 100
min_index = 0
max_item = 0
max_index = 0


for i in range(len(array)):
    if array[i] < min_item:
        min_item = array[i]
        min_index = i
    if array[i] > max_item:
        max_item = array[i]
        max_index = i

sum_items = 0
if min_index > max_index:
    min_index, max_index = max_index, min_index

for i in range(min_index + 1, max_index):
    sum_items += array[i]

print(f"MIN = {min_item}, MAX = {max_item}")
print(f"Сумма элементов: {sum_items}")
