# -*- coding: utf-8 -*-
from datetime import datetime
import random


def mergesort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = random.choice(arr)
        ind = arr.index(pivot)
        arr.pop(ind)

        less_1 = [i for i in arr[ind:] if i <= pivot]
        less_2 = [i for i in arr[:ind] if i <= pivot]
        greater_1 = [i for i in arr[ind:] if i > pivot]
        greater_2 = [i for i in arr[:ind] if i > pivot]

        return mergesort(less_1) + mergesort(greater_1) + [pivot] + mergesort(less_2) + mergesort(greater_2)


print mergesort([3, 4, 11, 2, 5, 9, 15])