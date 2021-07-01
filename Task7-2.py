"""
2) Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
   на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from numpy import random


def merge_sort(arr):

    def merge(left, right):
        res = []
        i, j = 0, 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        if i < len(left):
            res.extend(left[i:])
        else:
            res.extend(right[j:])

        return res

    def div_half(lst):

        if len(lst) == 1:
            return lst

        elif len(lst) == 2:
            if lst[0] <= lst[1]:
                return lst
            else:
                return lst[::-1]

        else:
            return merge(div_half(lst[:len(lst) // 2]), div_half(lst[len(lst) // 2:]))

    return div_half(arr)


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [round(random.sample() * 50, 2) for _ in range(SIZE)]

print(f'Исходный массив:\n{array}')
print(f'Конечный массив:\n{merge_sort(array)}')
