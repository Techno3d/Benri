from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys

class mainWindow(QMainWindow):
    super.__init__()

    self.setWindowTitle("Main Window") # Set window title

    self.setGeometry(100, 100, 500, 500) # Set window size

    self.setUi() # Set UI

    self.show() # Show window

    setWindowOpacity(self, 0.9) # Set window opacity

def setUi(self):
    print("Set UI")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())