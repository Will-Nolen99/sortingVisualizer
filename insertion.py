from draw import draw_sort

def insertion(array, win): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(array)): 
  
        key = array[i].val 

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