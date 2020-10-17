from draw import draw_sort

def bubble(array, win):
                
    length = len(array) 
    
    for i in range(length): 
         
        for j in range(0, length-i-1): 
  
            if array[j].val > array[j+1].val : 
                array[j], array[j+1] = array[j+1], array[j] 
  
        array[length - i - 1].status = "sorted"
        draw_sort(array, win)
    return array
     