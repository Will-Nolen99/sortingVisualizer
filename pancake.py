from draw import draw_sort

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
      
    curr_size = n 
    while curr_size > 1: 

        mi = findMax(array, curr_size) 
  
        if mi != curr_size-1: 

            flip(array, mi) 
  
            flip(array, curr_size-1) 
        curr_size -= 1    
        
        draw_sort(array, win)
    return array
