from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
app = QApplication(sys.argv)
mainWindow = QMainWindow()
mainWindow.setWindowTitle("Main Window")
mainWindow.setWindowOpacity(0.9)
mainWindow.setGeometry(100, 100, 500, 500)
mainWindow.show()

sys.exit(app.exec_())

# def setUi(self):
#     print("Set UI")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = mainWindow()
#     sys.exit(app.exec_())