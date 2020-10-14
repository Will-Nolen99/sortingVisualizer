import pygame as pg
import time
import random as r
import sorts





def main():
    
    
    
    sorts = {
        "bubble":sorts.bubble   
    }
    
    (width, height) = (500, 500)
    window = pg.display.set_mode((width, height))
    pg.display.set_caption("Sorting Visualizer")
    mode = menu
    
    
    array = [r.randint(0, 100) for i in range(100)]
    
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False










if __name__ == '__main__':
    main()