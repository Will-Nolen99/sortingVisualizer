import pygame as pg
import sorts
import menu
from element import make_array
from draw import draw_menu


def main():
    
    
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
    
    main_menu = menu.create_menu(window)
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
        draw_menu(array, window, main_menu)


    pg.quit()





if __name__ == '__main__':
    pg.init()
    (width, height) = (1500, 1000)
    window = pg.display.set_mode((width, height))
    pg.display.set_caption("Sorting Visualizer")
    main()