import pygame as pg
import random as r
import sorts
import menu
from noise import snoise2
from sorts import Element

'''

   colors                Hex                 rgb
   ######               ######              ######

Raisin Black            171A21            (23, 26, 33)
Cadet                   617073            (97, 112, 115)
Periwinkle Crayola      C3C9E9            (195, 201, 233)
Sea Green Crayola       44FFD1            (68, 255, 209)
Medium Spring Green     40F99B            (64, 249, 155)
Brink Pink              E85D75            (232, 93, 117)

'''



def main():
    
    
    (width, height) = (1500, 1000)
    window = pg.display.set_mode((width, height))
    pg.display.set_caption("Sorting Visualizer")
    
    
    algorithm = {
        "Selection sort": sorts.selection,
        "Bubble sort": sorts.bubble,
        "Quick sort": sorts.quick,
        "Shell sort": sorts.shell,
        "Gravity sort": sorts.gravity,
        "Insertion sort": sorts.insertion,
        "Radix sort": sorts.radix,
        "Pancake sort": sorts.pancake
        
     
    }
    
    
    
    background = (23, 26, 33)
    
    main_menu = create_menu(window)
    
    
    
    array = make_array(main_menu.elements)
    
    running = True
    while running:
        
        mouse_x, mouse_y = pg.mouse.get_pos()
        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            if event.type == pg.MOUSEBUTTONDOWN:
                choice = main_menu.clicked()
                if choice not in algorithm and choice is not None:
                    array = make_array(main_menu.elements)
                elif choice in algorithm:
                    for num in array:
                        num.status = "normal"
                    array = algorithm.get(choice)(array, window)

        #Updates
        main_menu.update(mouse_x, mouse_y)
        
        
        
        #Draw
        #window.fill(background)
        
        draw(array, window, main_menu)
        pg.display.update()

            
        
        
    pg.quit()



  




def create_menu(win):
    m = menu.Menu(win)
    
    #first columns
    bubble = menu.Button("Bubble sort", (25, 25), (150, 50), win)
    quick = menu.Button("Quick sort", (25, 100), (150, 50), win)
    selection = menu.Button("Selection sort", (25, 175), (150, 50), win)
    shell = menu.Button("Shell sort", (25, 250), (150, 50), win)
    
    
    #second column
    gravity = menu.Button("Gravity sort", (200, 175), (150, 50), win)
    insertion = menu.Button("Insertion sort", (200, 250), (150, 50), win)
    radix = menu.Button("Radix sort", (200, 25), (150, 50), win)
    pancake = menu.Button("Pancake sort", (200, 100), (150, 50), win)
    
    
    
    #non sort buttons
    up = menu.Button("-10", (500, 75), (75, 45), win)
    down = menu.Button("+10", (600, 75), (75, 45), win)
    
    up100 = menu.Button("-100", (500, 140), (75, 45), win)
    down100 = menu.Button("+100", (600, 140), (75, 45), win)
    
    generate = menu.Button("New array", (800, 25), (115, 50), win)
    
    
    m.add_button(up100)
    m.add_button(down100)
    
    m.add_button(generate)
    m.add_button(pancake)
    m.add_button(radix)
    m.add_button(insertion)
    m.add_button(gravity)
    m.add_button(shell)
    m.add_button(bubble)
    m.add_button(quick)
    m.add_button(selection)
    m.add_button(up)
    m.add_button(down)
    
    return m



def draw(array, win, men, array2=None):
    
    
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
    
    men.draw_elements()
    
    if array2 is not None:
        for i, num in enumerate(array2):
            pg.draw.rect(win, colors.get(num.status),  (i * element_width, h - num.val, element_width, num.val))
            if len(array) <= 500:
                pg.draw.rect(win, (97, 112, 115),  (i * element_width, h - num.val, element_width, num.val), 1)
    
    
    for i, num in enumerate(array):
        pg.draw.rect(win, colors.get(num.status),  (i * element_width, h - num.val, element_width, num.val))
        if len(array) <= 500:
            pg.draw.rect(win, (97, 112, 115),  (i * element_width, h - num.val, element_width, num.val), 1)







def make_array(length):
    t = r.randint(0, 10000)
    array = [ 500 * abs(snoise2(.005 * i, t)) for i in range(length)]
    array = list(map(lambda x: Element(x), array))
    
    return array





if __name__ == '__main__':
    pg.init()
    main()