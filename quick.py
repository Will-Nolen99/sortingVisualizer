from draw import draw_sort

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
    
    
def partition(array,low,high, win): 
    i = ( low-1 )         # index of smaller element 
    pivot = array[high].val     # pivot 
  
  
    for j in range(low , high): 
        # If current element is smaller than the pivot    
        if   array[j].val < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            array[i].val,array[j].val = array[j].val,array[i].val 

    draw_sort(array, win)

    array[i+1].val,array[high].val = array[high].val,array[i+1].val 
    return ( i+1 ) 
  

def quickSort(array,low,high, win): 
    
    
    if low < high: 

        pi = partition(array,low,high, win) 

        quickSort(array, low, pi-1, win) 
        
        for num in range(low, pi): 
            array[num].status = "sorted"
        quickSort(array, pi+1, high, win) 
        for num in range(pi, high): 
            array[num].status = "sorted"
        
            
def isSorted(array):
    for i, num in enumerate(array):
        if i + 1 != len(array) and  num.val > array[i + 1].val:
            return False
    return True