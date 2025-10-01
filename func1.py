# Функции
from tkinter.font import names
import statistics

temperatures = [13, 11, 7, -1, 7, 9, 10]


# вычислить среднюю, минимальную, максимальную


# def hello(name):
#    print('Привет,', name)


# def goodbye(name):
#    print('Пока,', name)


# hello("Пётр")
# goodbye("Дима")


def min_vale(temperatures):
    min_val = temperatures[0]  # присваиваем минимум значение первого элемента
    for num in temperatures:
        if num < min_val:
            min_val = num
    return min_val  # возвращение значения и завершение работы


def max_vale(temperatures):
    max_val = temperatures[0]  # присваиваем максимум значение первого элемента
    for num in temperatures:
        if num > max_val:
            max_val = num
    return max_val  # возвращение значения и завершение работы


def round_len_and_sqare(radius):
    print(f'Площадь круга с радиусов {radius} = '
          f'{radius ** 2 * 3.14}')
    print(f'Длина окружности с радиусом {radius} = '
          f'{radius * 2 * 3.14}')


def avarage(temperatures):
    count = len(temperatures)  # число элементов в списке
    summ = 0  # изначальная сумма нулевая
    for num in temperatures:
        summ += num
    return summ / count


print(max_vale(temperatures))
print(min_vale(temperatures))
print(avarage(temperatures))
print(sum(temperatures) / len(temperatures))
print(statistics.mean(temperatures))  # встроенной нет, но есть библиотека
round_len_and_sqare(5)
