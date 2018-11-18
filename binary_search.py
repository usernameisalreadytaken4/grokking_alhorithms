# -*- coding: utf-8 -*-


def binary_search(_list, item):
    low = 0
    high = len(_list) - 1
    count = 1
    while low <= high:
        print 'iteration:', count
        mid = (low + high) / 2
        guess = _list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
        count += 1


my_list = [1, 3, 5, 7, 9]

print binary_search(my_list, 3)
print binary_search(my_list, -1)

# Упражнения: 
# 1: Имеется отсортированный список из 128 имен, и вы ищете в нем значение
# методом бинарного поиска. Какое максимальное количество
# проверок для этого может потребоваться?

import math

# ответ
print math.log(128, 2)

# 2: Предположим, размер списка увеличился вдвое. Как изменится максимальное
# количество проверок?

# ответ
print math.log(128*2, 2)