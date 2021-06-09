# https://drive.google.com/file/d/1hxS7QPmZt2F73hxym8GsVpu9jMtDrm6L/view?usp=sharing

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите трёхзначное число: '))

n1 = a // 100
n2 = (a % 100) // 10
n3 = a % 10

sum_a = n1 + n2 + n3
multi_a = n1 * n2 * n3

print("\nСумма цифр числа {} равна {}".format(a, sum_a))
print("Произведение цифр числа {} равно {}".format(a, multi_a))
