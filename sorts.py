import time
import pygame as pg

def selection(array, win):
    
    array = list(map(lambda x: Element(x), array))
    sorting = True
    
    while sorting:
        
        
        for i in range(len(array)):
            array[i].status = "current"
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            
            minimum = i
            for j in range(i + 1, len(array)):
                array[j].status = "current"
                swapped = False
                
                if array[j].val <= array[minimum].val:
                    swapped = True
                    
                    if minimum != i:
                        array[minimum].status = "normal"
                        
                    minimum = j
                    array[minimum].status = "selected"
                    
                draw(array, win)
                time.sleep(0.001)
                
                if array[j].status == "current":
                    array[j].status = "normal"   
                             
            
            
            array[i].status = "normal"
            
            array[i], array[minimum] = array[minimum], array[i]
            array[i].status = "sorted" 
            
                
            
            
            #draw(array, win)
            
        sorting = False
            
            
            
            
            
            
            
                    
                
                
                
                
                 
    
    
    
def draw(array, win):
    
    colors = {
            
        "normal":(195, 201, 233),
        "sorted":(68, 255, 209), 
        "current":(232, 93, 117),
        "selected":(64, 249, 155)
            
    }
        
    win.fill((23, 26, 33))
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
        

        
        
        