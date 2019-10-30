# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:46:02 2019

@author: GIDEON
"""

from random import randint

# create randomized, unsorted arrays for testing
def create_array(size = 10, max = 50):
    return [randint(0, max) for _ in range(size)]

def quicksort(a):

    if len(a) <= 1: return a

    smaller, equal, larger = [], [], []
    pivot = a[randint(0, len(a)-1)]

    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return quicksort(smaller) + equal + quicksort(larger)

# Testing the quicksort function
#a = create_array()
#print("Unsorted: {}", a)
#s = quicksort(a)
#print("Sorted: ", s)

# Benchmarking quicksort against mergesort...
n = [10, 100, 1000, 10000, 100000]
times = {'quick':[], 'merge':[]}
samples = 5
from time import time
from merge_sort import merge_sort

for size in n:
    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size, size)
        t0 = time()
        s = merge_sort(a)
        t1 = time()
        tot_time += (t1-t0)
    times['merge'].append(tot_time/float(samples))

    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size, size)
        t0 = time()
        s = quicksort(a)
        t1 = time()
        tot_time += (t1-t0)
    times['quick'].append(tot_time/float(samples))

print("n\tQuicksort\tMergesort")
print(40*"_")
for i, size in enumerate(n):
    print("%d\t%0.5f \t%0.5f"%(size,
                               times['quick'][i],
                               times['merge'][i]))