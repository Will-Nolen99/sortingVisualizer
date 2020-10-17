from draw import draw_sort

def shell(array, win): 
  
    # Start with a big gap, then reduce the gap 
    n = len(array) 
    gap = n//2
  
    while gap > 0: 
  
        for i in range(gap,n): 
            
            if gap == 1:
                array[i].status = "sorted"

            temp = array[i].val 

            j = i 
            while  j >= gap and array[j-gap].val >temp: 
                array[j].val = array[j-gap].val 
                j -= gap 
            
            # used to speed up visual
            if i % 5 == 0:
                draw_sort(array, win)

            array[j].val = temp 
        gap = gap // 2
    
    for element in array:
        element.status = "sorted"
    draw_sort(array, win)
    return array