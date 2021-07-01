"""
1) Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
   на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
"""

from random import randint


def bubble_sort(lst):
    n = 1
    while n < len(lst):
        flag = 1
        for i in range(SIZE - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = 0
        if flag:
            return
        n += 1


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив:\n{array}')
bubble_sort(array)
print(f'Конечный массив:\n{array}')
