def my_abs(x: int = 0) -> int:  # используем значение по умолчанию для х
    """
    Функция для вычисления модуля целого числа
    :param x: целое
    :return: модуль в виде целого числа
    """
    if x >= 0:
        return x
    return -x


def get_coordinates() -> tuple:
    """
    Возвращает координаты
    :return: в виде кортежа
    """
    return 45, 14, 35


def greet_to_all(names: list) -> None:
    """
    Здоровается со всеми именами в списке
    :param names: в виде списка
    :return: ничего не возвращает
    """
    for name in names:
        print('Hello,', name)


x, y, z = get_coordinates()  # 1-й способ
res = get_coordinates()  # 2-й способ
print(f'X={x}, Y={y}, Z={z}')  # 1-й способ
print(f'X={res[0]}, Y={res[1]}, Z={res[2]}')  # 2-й способ
print(my_abs(-5))  # если в скобках ничего нету/пусто, то будет 0 выдавать
