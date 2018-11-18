# -*- coding: utf-8 -*-
import random


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


print quicksort([10, 2, 15, 2, 3, 10, 15])


def quicksort_with_random(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = random.choice(arr)
        ind = arr.index(pivot)

        less = [i for i in arr[ind:] if i <= pivot]
        greater = [i for i in arr[ind:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


print quicksort([10, 2, 15, 2, 3, 10, 15])
