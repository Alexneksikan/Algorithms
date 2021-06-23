"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import namedtuple

Company = namedtuple('Company', 'name q1 q2 q3 q4 year')

n = int(input('Введите количество предприятий: '))
companies = [0 for _ in range(n)]
profit_sum = 0

for i in range(n):
    name = input(f'Введите название {i + 1} предприятия: ')
    quarters = [float(j) for j in input('Введите через проблем прибыль в каждом квартале: ').split()]

    year = 0
    for q in quarters:
        year += q

    profit_sum += year
    companies[i] = Company(name, *quarters, year)

profit_average = profit_sum / n

less = []
more = []

for i in range(n):
    if companies[i].year < profit_average:
        less.append(companies[i])
    elif companies[i].year >= profit_average:  # сюда же включаю предприятия, прибыль которых равна средней,
        # хотя в условии задачи не сказано, что делать с такими предприятиями
        more.append(companies[i])

print(f'\nСредняя годовая прибыль по всем предприятиям: {profit_average: .2f}')

print(f'\nПредприятия с прибылью ниже {profit_average: .2f}')
for item in less:
    print(f'Предприятие "{item.name}", прибыль {item.year: .2f}')

print(f'\nПредприятия с прибылью выше {profit_average: .2f}')
for item in more:
    print(f'Предприятие "{item.name}", прибыль {item.year: .2f}')
