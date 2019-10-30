# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 18:18:40 2019

@author: GIDEON
"""

from random import randint

# create array of length 'size'
# array integers are of range (0 : max)
def create_array(size = 10, max = 50):
    new_arr = [randint(0, max) for _ in range(size)]
    return new_arr

def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = True
    return arr

# returns true if the passed array is sorted, false otherwise
def is_sorted(arr):
    sorted_arr = sorted(arr)
    return arr == sorted_arr

# Benchmarks the bubble sort against the built in python sorting method
def benchmark(n = [10,100,1000,10000]):

    from time import time

    b0 = [] # bubble sort times
    b1 = [] # built in sort times

    for length in n:
        a = create_array(length, length)

        t0 = time()
        s = sorted(a) # sort with built in
        t1 = time()
        b1.append(t1-t0) # record built in time

        t0 = time()
        s = bubble_sort(a) # sort with bubble sort
        t1 = time()
        b0.append(t1-t0) # record bubble sort time

    print("\n \tBuilt-In\tBubble Sort")
    print("___________________________________________")
    for i, cur_n in enumerate(n):
        print("%d\t%0.5f \t%0.5f"%(cur_n, b1[i], b0[i]))

benchmark()

# Testing the bubblesort function
a = create_array()
print(a)
a = bubble_sort(a)
print(a)
print(is_sorted(a))