from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QCheckBox, QDockWidget, QLabel, QDesktopWidget
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
currentTask = None
taskList = []

app = QApplication(sys.argv)
mainWindow = QMainWindow()

widget = QDockWidget()
# taskListWidget = QDockWidget(mainWindow)

addBreak = QPushButton("Add Break", widget)
addBreak.move(100, 50)
addBreak.resize(200, 40)
addBreak.font().setPointSize(20)


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
    print(task)

createTask.clicked.connect(lambda: newTask())
    


class Task():
    id = 0

    def __init__(self, name):
        self.name = name
        self.status = False
        print(self.name)
        self.tasklabel = QLabel(widget)
        self.tasklabel.setText(self.name)
        self.tasklabel.setFont(QFont('Arial', 20))
        
        self.tasklabel.move(100, 200 + (Task.id * 40))
        self.tasklabel.resize(200, 40)
        self.tasklabel.show()
        self.checkBox = QCheckBox(widget)
        self.checkBox.move(460, 200 + (Task.id * 40))
        self.checkBox.resize(40, 40)
        self.checkBox.show()
        

        def setStatus(self, status):
            self.status = status

        Task.id += 1
        self.checkBox.stateChanged.connect(lambda: setStatus(self, self.checkBox.isChecked()))
        def getStatus(self):
            return self.status
        def getName(self):
            return self.name
        
    

    

# class Break(Task):
#     super().__init__(self, "Break")
#     self.time = 300

#     while (self.checkbox.isChecked()):
#         self.time -= 1
#         time.sleep(1)
#         if (self.time == 0):
#             self.checkbox.setChecked(False)
#             self.time = 300


    





mainWindow.setWindowTitle("Benri")
mainWindow.setWindowOpacity(0.8)
mainWindow.setGeometry(100, 100, 500, 1080)
# mainWindow.setStyleSheet("background-color: #000000; color: #ffffff;")
mainWindow.addDockWidget(Qt.LeftDockWidgetArea, widget)
# mainWindow.addDockWidget(Qt.RightDockWidgetArea, taskListWidget)

mainWindow.setWindowFlags(Qt.WindowStaysOnTopHint)
mainWindow.setWindowFlags(Qt.FramelessWindowHint)
# mainWindow.setWindowFlags(Qt.WindowCloseButtonHint)
mainWindow.move(QDesktopWidget().availableGeometry().topLeft() - mainWindow.frameGeometry().topLeft())

# mainWindow.move()
mainWindow.show()



if __name__ == "__main__":
    sys.exit(app.exec_())


# def setUi(self):
#     print("Set UI")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = mainWindow()
#     sys.exit(app.exec_())