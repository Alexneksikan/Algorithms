"""
3) Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
"""
from random import randint


def median(lst):
    """
    Для каждого элемента массива подсчитываем количество чисел меньше и больше данного числа.
    Если эти значения равны, мы нашли медиану и выходим из процедуры.
    Однако алгоритм точно работает только при условии, что все элементы массива уникальны.
    Если в массиве есть некоторое количество чисел-медиан, то алгоритм может работать неправильно.
    """
    median_number = None
    diff = SIZE
    for i in range(len(lst)):
        more = less = 0
        for j in range(len(lst)):
            if i != j:
                if lst[j] < lst[i]:
                    less += 1
                if lst[j] > lst[i]:
                    more += 1

        if less == more:
            """ Если количество чисел слева и справа одинаковое, то решение готово """
            return lst[i]
        if abs(less - more) < diff:
            """
            На случай, если у медианы есть дубли, ищем элемент с наименьшей разностью
            количеств меньших и бОльших элементов. Считаем, что это медиана.
            Однако при достаточно большом количестве копий числа-медианы этот анализ не работает.
            """
            diff = abs(less - more)
            median_number = lst[i]

    return median_number


def median_search(lst, first, last):

    lst = lst.copy()
    ind = len(lst) // 2

    if first >= last:
        return lst[ind]

    pillar = lst[ind]
    i = first
    j = last

    while i <= j:
        while lst[i] < pillar:
            i += 1
        while lst[j] > pillar:
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    if ind < i:
        lst[ind] = median_search(lst, first, j)
    elif j < ind:
        lst[ind] = median_search(lst, i, last)

    return lst[ind]


def bubble_sort(lst):
    n = 1
    while n < len(lst):
        flag = 1
        for i in range(SIZE - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = 0
        if flag:
            return
        n += 1


SIZE = 11
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Массив:\n{array}')
print(f'Медиана по моему алгоритму: {median(array)}')
print(f'Медиана (алгоритм медиана медиан): {median_search(array, 0, len(array) - 1)}')

bubble_sort(array)
print(f'\nСортируем для проверки:\n{array}')
print(f'Медиана: {array[int(len(array) / 2)]}')
