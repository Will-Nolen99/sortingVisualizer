import pygame as pg






def create_menu(win):
    m = Menu(win)
    
    #first columns
    bubble = Button("Bubble sort", (25, 25), (150, 50), win)
    quick = Button("Quick sort", (25, 100), (150, 50), win)
    selection = Button("Selection sort", (25, 175), (150, 50), win)
    shell = Button("Shell sort", (25, 250), (150, 50), win)
    
    
    #second column
    gravity = Button("Gravity sort", (200, 175), (150, 50), win)
    insertion = Button("Insertion sort", (200, 250), (150, 50), win)
    radix = Button("Radix sort", (200, 25), (150, 50), win)
    pancake = Button("Pancake sort", (200, 100), (150, 50), win)
    
    
    
    #non sort buttons
    up = Button("-10", (500, 75), (75, 45), win)
    down = Button("+10", (600, 75), (75, 45), win)
    
    up100 = Button("-100", (500, 140), (75, 45), win)
    down100 = Button("+100", (600, 140), (75, 45), win)
    
    generate = Button("New array", (800, 25), (115, 50), win)
    
    
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


class Menu:
    
    def __init__(self, win):
        self.elements = 1500
        self.buttons = []
        self.win = win
        self.font = pg.font.SysFont('arial', 25)
        self.textsurface = self.font.render(f"Array Elements: {self.elements}", False, (68, 255, 209))
        self.w, self.h = pg.display.get_surface().get_size()
        
    def add_button(self, button):
        self.buttons.append(button)
        
    def draw_elements(self):
        self.win.blit(self.textsurface, (500, 25))
        for button in self.buttons:
            button.draw()
    
    def update(self, x, y):
        for button in self.buttons:
            button.update(x, y)
            
        self.textsurface = self.font.render(f"Array Elements: {self.elements}", False, (68, 255, 209))
            
    def clicked(self):

        for button in self.buttons:
            click = button.clicked()
            if click == "+10":
                if self.elements < self.w:
                    self.elements += 10
                return "modification"
            elif click == "-10":
                if self.elements > 10:
                    self.elements -= 10
                return "modification"     
            elif click == "+100":
                if self.elements < self.w - 100:
                    self.elements += 100
                return "modification"
            elif click == "-100":
                if self.elements > 100:
                    self.elements -= 100
                return "modification "       
            elif click:
                return click
            
    
    
    
    
    
class Button:
    
    def __init__(self, text, coords, ext, win):
        self.text = text
        self.coords = coords
        self.rect = pg.Rect(coords, ext)
        self.win = win
        self.color = (195, 201, 233)
        self.font = pg.font.SysFont('arial', 25)
        self.textsurface = self.font.render(self.text, False, (68, 255, 209))
        self.hovered = False
        
        
    def draw(self):
        pg.draw.rect(self.win, self.color, self.rect, 2)
        self.win.blit(self.textsurface, (self.coords[0] + 10, self.coords[1] + 10))
    
    def update(self, x, y):
        
        if self.rect.collidepoint(x,y):
            self.hovered = True
            self.color = (97, 112, 115)
        else: 
            self.hovered = False
            self.color = (195, 201, 233)
            
    
    def clicked(self):
        return self.text if self.hovered else False