import pygame as pg



def draw_menu(array, win, menu, array2=None):
    
    
    colors = {
            
        "normal":(195, 201, 233),
        "sorted":(68, 255, 209), 
        "current":(232, 93, 117),
        "selected":(64, 249, 155),
        "background":(23, 26, 33)
            
    }
        
    win.fill(colors.get("background"))
    
    w, h = pg.display.get_surface().get_size()
    elements = len(array)
    element_width = w / elements
    
    menu.draw_elements()
    
    if array2 is not None:
        for i, num in enumerate(array2):
            pg.draw.rect(win, colors.get(num.status),  (i * element_width, h - num.val, element_width, num.val))
            if len(array) <= 500:
                pg.draw.rect(win, (97, 112, 115),  (i * element_width, h - num.val, element_width, num.val), 1)
    
    
    for i, num in enumerate(array):
        pg.draw.rect(win, colors.get(num.status),  (i * element_width, h - num.val, element_width, num.val))
        if len(array) <= 500:
            pg.draw.rect(win, (97, 112, 115),  (i * element_width, h - num.val, element_width, num.val), 1)
    
    pg.display.update()
            
            
            
def draw_sort(array, win, array2=None):
    

    win.fill((23, 26, 33))

    colors = {
            
        "normal":(195, 201, 233),
        "sorted":(68, 255, 209), 
        "current":(232, 93, 117),
        "selected":(64, 249, 155)
            
    }
        
    
    w, h = pg.display.get_surface().get_size()
    elements = len(array)
    element_width = w / elements
    
    
    if array2 is not None:
        for i, num in enumerate(array2):
            pg.draw.rect(win, colors.get(num.status),  (i * element_width, h - num.val, element_width, num.val))
            if len(array) <= 500:
                pg.draw.rect(win, (97, 112, 115),  (i * element_width, h - num.val, element_width, num.val), 1)
    
    
    for i, num in enumerate(array):
        pg.draw.rect(win, colors.get(num.status),  (i * element_width, h - num.val, element_width, num.val))
        if len(array) <= 500:
            pg.draw.rect(win, (97, 112, 115),  (i * element_width, h - num.val, element_width, num.val), 1)
            

    pg.display.update()