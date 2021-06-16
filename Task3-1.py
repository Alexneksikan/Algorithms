"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

MIN_ITEM = 2
MAX_ITEM = 99
START_N = 2
FINISH_N = 9
stat_array = [0] * 8

for i in range(MIN_ITEM, MAX_ITEM + 1):
    for j in range(START_N, FINISH_N + 1):
        if i % j == 0:
            stat_array[j - 2] += 1

for j in range(START_N, FINISH_N + 1):
    print(j, ' - ', stat_array[j - 2])
