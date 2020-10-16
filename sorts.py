import time
import pygame as pg

def selection(array, win):
    
    sum_time = 0.0
    comparisons = 0
    access = 0
    array = list(map(lambda x: Element(x), array)) 
        
        
    for i in range(len(array)):
        array[i].status = "current"
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            
        minimum = i
        for j in range(i + 1, len(array)):
            #time.sleep(.5)
            array[j].status = "current"
            swapped = False
                
            comparisons += 1
            first = time.time()
            if array[j].val <= array[minimum].val:

                swapped = True
                access += 2
                    
                if minimum != i:
                    array[minimum].status = "normal"
                        
                minimum = j
                array[minimum].status = "selected"
                    

            
            draw(array, win)
                
            if array[j].status == "current":
                array[j].status = "normal"   
            
        array[i].status = "normal"

        array[i], array[minimum] = array[minimum], array[i]

            
        array[i].status = "sorted"

    for element in array:
        element.status = "sorted"
        draw(array, win)
    pause()        
            

            
            
            
            
            
            
            
                    
def bubble(array, win):
    

    array = list(map(lambda x: Element(x), array))
                
    length = len(array) 
    
    for i in range(length): 
        
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
        
        
        # Last i elements are already in place 
        for j in range(0, length-i-1): 
            array[j].status = "current"
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if array[j].val > array[j+1].val : 
                array[j], array[j+1] = array[j+1], array[j] 
                array[j].status = "selected"

            draw(array, win)
            array[j].status = "normal"
            
        array[length - i - 1].status = "sorted"

    for element in array:
        element.status = "sorted"
        draw(array, win)
    pause()  
        
def quick(array, win):
    length = len(array)
    array = list(map(lambda x: Element(x), array))
    quickSort(array, 0, length-1, win)
    for element in array:
        element.status = "sorted"
        draw(array, win)
    pause()
    
    
    
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
        array[i].status = "selected"    
    
        if   array[j].val < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            array[i].val,array[j].val = array[j].val,array[i].val 

            
        
        draw(array, win)
        
  
    
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
        
        array[low].status = "current"
        array[high].status = "current"
        pi = partition(array,low,high, win) 
        array[pi].status = "sorted"

        
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(array, low, pi-1, win) 
        
        for num in range(low, pi - 1): 
            array[num].status = "sorted"
        
        quickSort(array, pi+1, high, win) 
        array[pi].status = "sorted"
        
        
        
def shell(array, win): 
    array = list(map(lambda x: Element(x), array))
  
    # Start with a big gap, then reduce the gap 
    n = len(array) 
    gap = n//2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = array[i].val 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and array[j-gap].val >temp: 
                array[j].val = array[j-gap].val 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            array[j].val = temp 
            draw(array, win)
            
        gap = gap // 2
    
    pause()
        
          
    
    
def pause():
    while True:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    return

    
    
def draw(array, win):
    
    
    win.fill((23, 26, 33))

    
    colors = {
            
        "normal":(195, 201, 233),
        "sorted":(68, 255, 209), 
        "current":(232, 93, 117),
        "selected":(64, 249, 155)
            
    }
        
    
    w, h = pg.display.get_surface().get_size()
    elements = len(array)
    element_width = w // elements
    
    for i, num in enumerate(array):
        pg.draw.rect(win, colors.get(num.status),  (i * element_width, h - num.val, element_width, num.val))
        pg.draw.rect(win, (97, 112, 115),  (i * element_width, h - num.val, element_width, num.val), 1)
    
    

    
    pg.display.update()
    
    
    
    


class Element:
    def __init__(self, val):
        self.val = val
        self.status = "normal"
        

        
        
        