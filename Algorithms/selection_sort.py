# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:38:07 2019

@author: GIDEON
"""

def create_array(size = 10, max = 50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

# performs the selection sort algorithm on the passed list,
    # returns the sorted version
def selection_sort(a):
    sort_len = 0 # length of current sorted portion
    while sort_len < len(a):
        min_idx = None # index of smallest item found
        for i, elem in enumerate(a[sort_len:]):
            # check curent element to see if smallest
            if min_idx == None or elem < a[min_idx]:
                # update with current smallest
                min_idx = i + sort_len
        a[sort_len], a[min_idx] = a[min_idx], a[sort_len]
        sort_len += 1
    return a

# benchmarking selection sort against built-in python sort and bubble sort
bub_times, sel_times, builtin_times = [], [], []

from time import time
from bubble_sort import bubble_sort

n = [10,100,1000,10000]

for length in n:
    a = create_array(length, length)

    t0 = time()
    s = sorted(a)
    t1 = time()
    builtin_times.append(t1-t0)

    t0 = time()
    s = bubble_sort(a)
    t1 = time()
    bub_times.append(t1-t0)

    t0 = time()
    s = selection_sort(a)
    t1 = time()
    sel_times.append(t1-t0)

print("n \tBuilt-In\tBubble\tSelection")
print("____________________________________________")
for i, cur_n in enumerate(n):
    print("%d\t%0.5f \t%0.5f \t%0.5f"%(cur_n,
                                       builtin_times[i],
                                       bub_times[i],
                                       sel_times[i]))


# Test
a = create_array()
print("Unsorted: ", a)
a = selection_sort(a)
print("Sorted: ", a)
