"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
   Вывести на экран это число и сумму его цифр.
"""


def summa(x):
    if x == 0:
        return 0
    return x % 10 + summa(x // 10)


number = 1          # текущее число
target_number = 0   # искомое число
number_sum = 0      # сумма цифр текущего числа
target_sum = 0      # сумма цифр искомого числа

while number != 0:
    number = int(input('Введите натуральное число (ноль для завершения)'))
    number_sum = summa(number)
    if number_sum > target_sum:
        target_sum = number_sum
        target_number = number

print(f"\nЧисло: {target_number} \nСумма цифр: {target_sum}")
