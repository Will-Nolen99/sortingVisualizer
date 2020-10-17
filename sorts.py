import time
import pygame as pg
from draw import draw_sort

def selection(array, win):
    
    sum_time = 0.0
    comparisons = 0
    access = 0

        
        
    for i in range(len(array)):
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            
        minimum = i
        for j in range(i + 1, len(array)):
            #time.sleep(.5)

            swapped = False
                
            comparisons += 1
            first = time.time()
            if array[j].val <= array[minimum].val:

                swapped = True
                access += 2
                    
                        
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
            
        array[i].status = "sorted"
        draw_sort(array, win)
    return array

     
            

            
            
            
            
            
            
            
                    
def bubble(array, win):
    

                
    length = len(array) 
    
    for i in range(length): 
        
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
        
        
        # Last i elements are already in place 
        for j in range(0, length-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if array[j].val > array[j+1].val : 
                array[j], array[j+1] = array[j+1], array[j] 
  
        array[length - i - 1].status = "sorted"
        draw_sort(array, win)
    return array
     
        
def quick(array, win):
    
    if isSorted(array):
        for num in array:
            num.satus = "sorted"
        return array
    
    length = len(array)
    quickSort(array, 0, length-1, win)
    for element in array:
        element.status = "sorted"
    draw_sort(array, win)
    return array
    
    
    
# Python program for implementation of Quicksort Sort 
  
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(array,low,high, win): 
    i = ( low-1 )         # index of smaller element 
    pivot = array[high].val     # pivot 
  
    #array[high].status = "selected"
  
    for j in range(low , high): 
        #array[i].status = "normal"
        # If current element is smaller than the pivot    
        if   array[j].val < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            array[i].val,array[j].val = array[j].val,array[i].val 

    draw_sort(array, win)

    array[i+1].val,array[high].val = array[high].val,array[i+1].val 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(array,low,high, win): 
    
    
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        
        pi = partition(array,low,high, win) 


        # Separately sort elements before 
        # partition and after partition 
        quickSort(array, low, pi-1, win) 
        
        for num in range(low, pi): 
            array[num].status = "sorted"
        quickSort(array, pi+1, high, win) 
        for num in range(pi, high): 
            array[num].status = "sorted"

        
        
        
def shell(array, win): 
  
    # Start with a big gap, then reduce the gap 
    n = len(array) 
    gap = n//2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
            
            if gap == 1:
                array[i].status = "sorted"
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = array[i].val 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and array[j-gap].val >temp: 
                array[j].val = array[j-gap].val 
                j -= gap 
            
            # used to speed up visual
            if i % 5 == 0:
                draw_sort(array, win)

            
  
            # put temp (the original a[i]) in its correct location 
            array[j].val = temp 
        gap = gap // 2
        
        

    
    for element in array:
        element.status = "sorted"
    draw_sort(array, win)
    return array

        
          
    
    

def gravity(array, win):



    up = [Element(0) for _ in array]
    down = array

    for num in up:
        num.status = "sorted"
    
    start_elements = len(down)
    count = 0
    size = 0
    
    length = len(down)
    sorting = True
    
    while size < length:
        
        count += 1
        
        old_len = 0
        for num in down:
            if num.val > 0:
                old_len += 1
                num.val -= 1
        
        new_len = 0
        for num in down:
            if num.val > 0:
                new_len += 1
        
        length_diff = old_len - new_len
        
        
        for i in range(length_diff ):
            up[size].val = count
            size += 1
             
        
        draw_sort(down, win, up)
        
    return up

        
    



def insertion(array, win): 
  

  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(array)): 
  
        key = array[i].val 
        
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < array[j].val : 
                array[j+1].val = array[j].val 
                j -= 1
        array[j+1].val = key 

        draw_sort(array, win)

    for num in array:
        num.status = "sorted"

    draw_sort(array, win)

    return array
    
    
    
    
def countingSort(array, exp1, win):
 
    n = len(array)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (array[i].val / exp1)
        count[int(index % 10)] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = (array[i].val / exp1)
        output[count[int(index % 10)] - 1] = array[i].val
        count[int(index % 10)] -= 1
        i -= 1
        
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(array)):
        array[i].val = output[i]
        if exp1 == 100:
            array[i].status ="sorted"
        
        
        if i % 5 == 0:
            draw_sort(array, win)
 
# Method to do Radix Sort
def radix(array, win):
 

    # Find the maximum number to know number of digits
 
    max1 = 0
    for num in array:
        if num.val > max1:
            max1 = num.val
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        countingSort(array, exp, win)
        exp *= 10
        time.sleep(.2)
        
    return array
    
    
    
    
    
# Reverses arr[0..i] */ 
def flip(array, i): 
    start = 0
    while start < i: 
        temp = array[start] 
        array[start] = array[i] 
        array[i] = temp 
        start += 1
        i -= 1
  
# Returns index of the maximum 
# element in arr[0..n-1] */ 
def findMax(array, n): 
    mi = 0
    for i in range(0,n): 
        if array[i].val > array[mi].val: 
            mi = i 
            
    array[mi].status = "sorted"
    return mi 
  
# The main function that  
# sorts given array  
# using flip operations 
def pancake(array, win): 
      
    n = len(array)  
      
    # Start from the complete 
    # array and one by one 
    # reduce current size 
    # by one 
    curr_size = n 
    while curr_size > 1: 
        # Find index of the maximum 
        # element in  
        # arr[0..curr_size-1] 
        mi = findMax(array, curr_size) 
  
        # Move the maximum element 
        # to end of current array 
        # if it's not already at  
        # the end 
        if mi != curr_size-1: 
            # To move at the end,  
            # first move maximum  
            # number to beginning  
            flip(array, mi) 
  
            # Now move the maximum  
            # number to end by 
            # reversing current array 
            flip(array, curr_size-1) 
        curr_size -= 1    
        
        draw_sort(array, win)
    return array


    
def pause():
    while True:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    return

    
    

    
    
    

def isSorted(array):
    for i, num in enumerate(array):
        if i + 1 != len(array) and  num.val > array[i + 1].val:
            return False
    return True
    
    


class Element:
    def __init__(self, val):
        self.val = val
        self.status = "normal"
        

        
        
        