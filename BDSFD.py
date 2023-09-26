import sys
import pygame
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

#mp3 or wav in the same dir
pygame.mixer.init()
easy = pygame.mixer.Sound('that_was_easy.mp3')


#main gui class - makes window with label containing gif with an invisible button in the center
class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Beleaguered Developer's Self-Flagellation Device")

        self.setGeometry(0, 0, 620, 580) # size of window in pixels

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 620, 580) #size of label in pixels...note the similarity to the window size
        self.label.setScaledContents(True)

        self.movie = QMovie("too_easy.gif")

        self.label.setMovie(self.movie)

        self.secret_button = QPushButton(self)
        self.secret_button.setStyleSheet("background-color: transparent; border: none;")
        self.secret_button.setGeometry(152, 120, 310, 220) #button sized to mimic easy button geometry

        self.clicky()

        self.show()
        self.movie.jumpToNextFrame()

    def clicky(self):

        self.secret_button.clicked.connect(self.WasClicked)

    def WasClicked(self):
        self.movie.start()
        easy.play()


BDSFD = QApplication(sys.argv)

app_window = AppWindow()

sys.exit(BDSFD.exec())
