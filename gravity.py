from draw import draw_sort
from element import Element

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
             
        
        
        print(size, length)
        draw_sort(down, win, up)
        
    return up