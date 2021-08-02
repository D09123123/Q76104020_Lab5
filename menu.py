import pygame
import os
from color_settings import SKY_BLUE, YELLOW


class UpgradeMenu:
    def __init__(self, x, y):
        self.menu_image = pygame.transform.scale(pygame.image.load("images/upgrade_menu.png"), (250, 250)) #import menu
        self.upgrade_image = pygame.transform.scale(pygame.image.load("images/upgrade.png"), (80, 40))     #import upgrade
        self.sell_image = pygame.transform.scale(pygame.image.load("images/sell.png"), (70, 70))           #import sell
        self.rect = self.menu_image.get_rect()      #get rectangle coordinate
        self.rect.center = (x, y)                   #center coordinate of rect
        self.x = x
        self.y = y
        self.__buttons = [Button(self.upgrade_image, "upgrade", self.x, self.y - 85),
                          Button(self.sell_image, "sell", self.x, self.y + 85)]  # (Q2) Add buttons here
                                                                                 # put the Button class in the list
    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu_image, self.rect)                        #draw menu on win
        # draw button
        # (Q2) Draw buttons here
        win.blit(self.upgrade_image,(self.x - 40  , self.y - 110))  #draw upgrade on win
        win.blit(self.sell_image,(self.x - 32, self.y + 60))        #draw sell on win
       

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons                                       #return the Button you click
       


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        if self.rect.collidepoint(x, y) == True:           # if the clicked mouse position is in the rectangle, return True
            return True
        return False                                       # else return False
    
    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name         #return the name of the button
        






