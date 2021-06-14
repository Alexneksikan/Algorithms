"""
https://drive.google.com/file/d/1Wm35KPuSPopL8dbcyW9eUmcPn5LAKJkT/view?usp=sharing

2. Посчитать четные и нечетные цифры введенного натурального числа.
   Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

number = int(input('Введите многозначное натуральное число: '))
even = 0  # количество чётных цифр
odd = 0   # количество нечётных цифр

for k in str(number):
    if int(k) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Число {number}: {even} чётных и {odd} нечётных цифры. ")
