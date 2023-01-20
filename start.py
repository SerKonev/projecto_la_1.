import pygame
import pygame_menu
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from start_scene import runin
from game_1 import game_main
from game_2 import Program
from game_3 import main
from end_scene import runi
from timer import maini

pygame.init()
surface = pygame.display.set_mode((800, 600))
game1 = True


def start_the_game():
    running = True
    running = runin
    if not runin():
        running = game_main()
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Program()
        ui.setupUi(MainWindow)
        ui.setup(MainWindow)
        MainWindow.show()
        running = main()
        runi()

def tim():
    runni = True
    runni = maini()






menu = pygame_menu.Menu('Добро пожаловать', 800, 600, theme=pygame_menu.themes.THEME_GREEN)
menu.add.text_input('Имя: ', default='Cool guy')
menu.add.button('Начать', start_the_game)
menu.add.button('Таймер', tim)
menu.add.button('Выйти', pygame_menu.events.EXIT)

menu.mainloop(surface)
