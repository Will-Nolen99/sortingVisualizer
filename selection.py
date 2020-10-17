from draw import draw_sort

def selection(array, win):
        
    for i in range(len(array)):
            
        minimum = i
        for j in range(i + 1, len(array)):
                
            if array[j].val <= array[minimum].val:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
            
        array[i].status = "sorted"
        draw_sort(array, win)
    return array