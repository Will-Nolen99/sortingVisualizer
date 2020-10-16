import pygame as pg
import random as r
import sorts
import menu
from noise import snoise2

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
    
    
    (width, height) = (1500, 500)
    window = pg.display.set_mode((width, height))
    pg.display.set_caption("Sorting Visualizer")
    
    
    algorithm = {
        "Selection sort": sorts.selection,
        "Bubble sort": sorts.bubble,
        "Quick sort": sorts.quick,
        "Shell sort": sorts.shell
     
    }
    
    
    
    background = (23, 26, 33)
    
    main_menu = create_menu(window)
    
    mode = "menu"
    
    running = True
    while running:
        
        mouse_x, mouse_y = pg.mouse.get_pos()
        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            if event.type == pg.MOUSEBUTTONDOWN:
                choice = main_menu.clicked()
                if choice is not None:
                    array = [ 500 * abs(snoise2(.01 * i, 0)) for i in range(main_menu.elements)]
                    print(array)
                    algorithm.get(choice)(array, window)

        #Updates
        main_menu.update(mouse_x, mouse_y)
        
        
        
        #Draw
        window.fill(background)
        
        main_menu.draw()
        pg.display.update()

            
        
        
    pg.quit()



  




def create_menu(win):
    m = menu.Menu(win)
    bubble = menu.Button("Bubble sort", (25, 25), (150, 50), win)
    quick = menu.Button("Quick sort", (25, 100), (150, 50), win)
    selection = menu.Button("Selection sort", (25, 175), (150, 50), win)
    shell = menu.Button("Shell sort", (25, 250), (150, 50), win)
    
    up = menu.Button("-10", (525, 75), (50, 50), win)
    down = menu.Button("+10", (600, 75), (50, 50), win)
    
    m.add_button(shell)
    m.add_button(bubble)
    m.add_button(quick)
    m.add_button(selection)
    m.add_button(up)
    m.add_button(down)
    
    return m


if __name__ == '__main__':
    pg.init()
    main()