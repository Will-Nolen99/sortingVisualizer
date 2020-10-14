import pygame as pg


class Menu:
    
    def __init__(self, win):
        self.elements = 100
        self.buttons = []
        self.win = win
        self.font = pg.font.SysFont('arial', 25)
        self.textsurface = self.font.render(f"Array Elements: {self.elements}", False, (68, 255, 209))
        
    def add_button(self, button):
        self.buttons.append(button)
        
    def draw(self):
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
                self.elements += 10
            elif click == "-10":
                if self.elements > 10:
                    self.elements -= 10
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