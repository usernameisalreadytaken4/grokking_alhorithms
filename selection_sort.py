# -*- coding: utf-8 -*-


def find_smalles(arr):
    """возвращаем индекс наименьшего элемента массива"""
    smallest = arr[0]
    smallest_index = 0

    for item in arr:
        if item < smallest:
            smallest = item
            smallest_index = arr.index(smallest)

    return smallest_index


def selection_sort(arr):
    """сортируем как можем"""
    new_arr = []

    while arr:
        smallest_index = find_smalles(arr)
        new_arr.append(arr.pop(smallest_index))

    return new_arr


print selection_sort([5, 3, 6, 2, 10])
