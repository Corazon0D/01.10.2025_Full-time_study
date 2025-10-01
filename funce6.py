# Функция, как объект и ф-ции высшего порядка
# map (функция как объект, iterable)
# filter (критерии отбора, iterable)
from string import capwords

words = ['Только','длинные', 'слова', 'пройдут', 'дальше', 'гидроэлектростанция+']

def double(x):
    return x * 2


def long_word(word): # слова, длина который больше 10
    return len(word) > 10


a = [1, 2, 3]
print(a)
b = map(double, a)
print(list(b))
# b = map(str, a)
# print(list(b))


a = (1,2,3)
lst = ['один','два', 'три']
print(a)
b = map(double, a)
cap = map(str.upper, lst)
print(list(cap))

res = filter(long_word, words)
print(list(res))