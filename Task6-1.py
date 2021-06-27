import sys

"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
ЗАДАЧА: Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

"""
Windows 10 64-разрядная, версия 10.0.19043
Python 3.9.4
"""


def info(obj):
    sum_memory = 0
    for var in obj:
        print(f'{type(var)=}, size={sys.getsizeof(var)}, {var=}')
        sum_memory += sys.getsizeof(var)
        if hasattr(var, '__iter__'):
            if hasattr(var, 'items'):
                for key, val in var.items():
                    info(key)
                    info(val)
    print(f'Затраты памяти: {sum_memory}')


a = int(input('Введите целое трехзначное число:'))

# Первый вариант решения:
n1 = a // 100
n2 = (a % 100) // 10
n3 = a % 10
sum_a1 = n1 + n2 + n3
multi_a1 = n1 * n2 * n3

print('\nПервый вариант:')
variables1 = (a, n1, n2, n3, sum_a1, multi_a1)
info(variables1)
"""
Первый вариант:
type(var)=<class 'int'>, size=28, var=567
type(var)=<class 'int'>, size=28, var=5
type(var)=<class 'int'>, size=28, var=6
type(var)=<class 'int'>, size=28, var=7
type(var)=<class 'int'>, size=28, var=18
type(var)=<class 'int'>, size=28, var=210
Затраты памяти: 168
"""

# Второй вариант решения:
sum_a2 = a // 100 + (a % 100) // 10 + a % 10
multi_a2 = (a // 100) * ((a % 100) // 10) * (a % 10)

print('\nВторой вариант:')
variables2 = (a, sum_a2, multi_a2)
info(variables2)
"""
Второй вариант:
type(var)=<class 'int'>, size=28, var=567
type(var)=<class 'int'>, size=28, var=18
type(var)=<class 'int'>, size=28, var=210
Затраты памяти: 84
"""

# Третий способ решения:
a = str(a)
sum_a3 = 0
multi_a3 = 1
digit = ''
for digit in a:
    sum_a3 += int(digit)
    multi_a3 *= int(digit)

print('\nТретий вариант:')
variables3 = (a, digit, sum_a3, multi_a3)
info(variables3)
"""
Третий вариант:
type(var)=<class 'str'>, size=52, var='567'
type(var)=<class 'str'>, size=50, var='7'
type(var)=<class 'int'>, size=28, var=18
type(var)=<class 'int'>, size=28, var=210
Затраты памяти: 158
"""

"""
ВЫВОД:
Наилучшим вариантом по выделенной памяти под переменные является второй вариант. В этом варианте используется 
наименьшее количество переменных типа int - только для хранения числа и результатов вычислений.
Первый вариант самый наглядный в смысле восприятия кода, однако обратной стороной этого является большое количество
дополнительно используемых переменных для промежуточных вычислений.
В третьем варианте используются строковые переменные. Соответственно при увеличении разрядности чисел затраты
памяти будут только увеличиваться.
"""
