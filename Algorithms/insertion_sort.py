# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:26:53 2019

@author: GIDEON
"""

def create_array(size = 10, max = 50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

def insertion_sort(a):
    for sort_len in range(1, len(a)):
        cur_item = a[sort_len] # next unsorted item
        insert_idx = sort_len # current index of item

        # iterate until we reach correct insert spot
        while insert_idx > 0 and cur_item < a[insert_idx - 1]:
            a[insert_idx] = a[insert_idx - 1] # shift
            insert_idx += -1 # decrement insert spot

        # insert item at correct spot
        a[insert_idx] = cur_item
    return a

# Benchmark against bubble sort and selection sort

def benchmark(n = [10,100,1000,10000]):
    from time import time
    from bubble_sort import bubble_sort
    from . import selection_sort
    ins_times, bub_times, sel_times = [], [], []

    for size in n:
        a = create_array(size, size)
        t0 = time()
        bubble_sort(a)
        t1 = time()
        bub_times.append(t1 - t0)

        a = create_array(size, size)
        t0 = time()
        selection_sort(a)
        t1 = time()
        sel_times.append(t1 - t0)

        a = create_array(size, size)
        t0 = time()
        insertion_sort(a)
        t1 = time()
        ins_times.append(t1 - t0)

    print("\nn\tInsertion\tBubble \tSelection")
    print(50 * "_")
    for i, size in enumerate(n):
        print("%d\t0.5f \t%0.5f \t%0.5f"%(size,
                                          ins_times[i],
                                          bub_times[i],
                                          sel_times[i]))

benchmark()


# Test
#a = create_array()
#print(a)
#s = insertion_sort(a)
#print(s)