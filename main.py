from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QCheckBox, QDockWidget, QLabel
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
taskList = []

app = QApplication(sys.argv)
mainWindow = QMainWindow()

widget = QDockWidget(mainWindow)
# taskListWidget = QDockWidget(mainWindow)


taskEntry = QLineEdit(widget)
taskEntry.move(100, 100)
taskEntry.resize(200, 40)
taskEntry.setPlaceholderText("Enter Task")
taskEntry.font().setPointSize(30)
taskEntry.font().setBold(True)
taskEntry.setAlignment(Qt.AlignCenter)
# taskEntry.setStyleSheet("background-color: #000000; color: #ffffff;")

createTask = QPushButton("Create Task", widget)
createTask.move(300, 100)
createTask.resize(200, 40)
createTask.font().setPointSize(20)
# createTask.setStyleSheet("background-color: #000000; color: #ffffff;")


def newTask():
    task = Task(taskEntry.text())
    taskList.append(task)
    taskEntry.setText("")

createTask.clicked.connect(lambda: newTask())
    


class Task():
    id = 0

    def __init__(self, name):
        self.name = name
        self.status = False
        print(self.name)
        self.tasklabel = QLabel(self.name, widget)
        self.checkBox = QCheckBox(widget)
        self.tasklabel.move(100, 200 + (Task.id * 40))
        self.tasklabel.resize(200, 40)
        self.checkBox.move(300, 200 + (Task.id * 40))
        self.checkBox.resize(200, 40)
        self.checkBox.stateChanged.connect(lambda: self.setStatus(self.checkBox.isChecked()))


        Task.id += 1
        
    # def createCheck(self):
    #     check = QCheckBox(self.name, widget)
    #     check.move(100, 200 + (Task.id * 40))
    #     check.resize(200, 40)
    #     check.stateChanged.connect(lambda: self.setStatus(check.isChecked()))

    # def setStatus(self, status):
    #     self.status = status

    
    





mainWindow.setWindowTitle("Main Window")
mainWindow.setWindowOpacity(0.75)
mainWindow.setGeometry(100, 100, 500, 500)
# mainWindow.setStyleSheet("background-color: #000000; color: #ffffff;")
mainWindow.addDockWidget(Qt.LeftDockWidgetArea, widget)
# mainWindow.addDockWidget(Qt.RightDockWidgetArea, taskListWidget)
mainWindow.show()

if __name__ == "__main__":
    sys.exit(app.exec_())


# def setUi(self):
#     print("Set UI")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = mainWindow()
#     sys.exit(app.exec_())