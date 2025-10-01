# Функции с переменным числом аргументов
from ctypes import HRESULT

# Распоковка с помощью *
x, *ostatok, y = 1, 2, 3, 4, 5, 6


def multipli(first=1, *rest):
    result = first
    for value in rest:
        result *= value
    return result


def multipli2(*rest: int, action='m') -> int or None:
    """
    Действия над переменным числом аргументов
    если задан неверный аргумент, то вернёт None
    :param rest: позиционные аргументы (числа)
    :param action: m - произведение< s - сумма
    :return: суумма или произведение аргументов
    """
    match action:
        case 'm':
            result = 1
            for value in rest:
                result *= value
        case 's':
            result = 0
            for value in rest:
                result += value
        case _:
            result = None
    return result


# result = 1
# for value in rest:
#    result *= value
#    return result


print(x, y)
print(ostatok)
print(multipli(5, 3, 4, 5))
print(multipli2(1, 2, 3, 4, 5, action='m'))
