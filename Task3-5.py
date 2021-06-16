"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"Исходный массив: {array}")

max_negative = -100

for i in range(len(array)):
    if 0 > array[i] > max_negative:
        max_negative = array[i]

print(f"Максимальный отрицательный элемент: {max_negative}")
