from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QCheckBox, QDockWidget, QLabel, QDesktopWidget
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
<<<<<<< HEAD
from benri_api import *

task = setup()
print(task[0].name)

=======
currentTask = None
>>>>>>> 9d39f32b840bb3b05aca8893cb6f73d2038b5cfb
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

createTask.clicked.connect(lambda: newTask())
    


class Task():
    numTasks = 0

    def __init__(self, name):
        
        self.name = name
        self.status = False
        
        self.tasklabel = QLabel(widget)
        self.tasklabel.setText(self.name)
        self.tasklabel.setFont(QFont('Arial', 20))
        self.id = Task.numTasks
        Task.numTasks += 1
        print(self.id)
        self.tasklabel.move(100, 140 + (self.id * 40))
        self.tasklabel.resize(400, 40)
        self.tasklabel.show()
        self.checkBox = QCheckBox(widget)
        self.checkBox.move(380, 140 + (self.id * 40))
        self.checkBox.resize(40, 40)
        self.checkBox.show()
        self.deleteButton = QPushButton("Delete", widget)
        self.deleteButton.move(400, 140 + (self.id * 40))
        self.deleteButton.resize(100, 40)
        self.deleteButton.show()
        self.deleteButton.clicked.connect(lambda: Task.delete(self))
        

    def delete(self):
        
        self.tasklabel.deleteLater()
        self.checkBox.deleteLater()
        self.deleteButton.deleteLater()
        self.tasklabel.hide()
        self.checkBox.hide()
        self.deleteButton.hide()
        Task.numTasks -= 1
        taskList.remove(self)
        for i in range(Task.numTasks):
            taskList[i].id = i
            taskList[i].tasklabel.move(100, 140 + (taskList[i].id * 40))
            taskList[i].checkBox.move(380, 140 + (taskList[i].id * 40))
            taskList[i].deleteButton.move(400, 140 + (taskList[i].id * 40))
        



        

        def setStatus(self, status):
            self.status = status

        
        self.checkBox.stateChanged.connect(lambda: setStatus(self, self.checkBox.isChecked()))
        def getStatus(self):
            return self.status
        def getName(self):
            return self.name
        
    
>>>>>>> 9d39f32b840bb3b05aca8893cb6f73d2038b5cfb

    

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
mainWindow.setWindowOpacity(0.5)
mainWindow.setGeometry(100, 100, 500, 1080)
# mainWindow.setStyleSheet("background-color: #000000; color: #ffffff;")
mainWindow.addDockWidget(Qt.LeftDockWidgetArea, widget)
# mainWindow.addDockWidget(Qt.RightDockWidgetArea, taskListWidget)


# mainWindow.setWindowFlags(Qt.WindowCloseButtonHint)
mainWindow.move(QDesktopWidget().availableGeometry().topLeft() - mainWindow.frameGeometry().topLeft())
mainWindow.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint))


# mainWindow.move()

mainWindow.setWindowIcon(QIcon('LOGO.png'))
mainWindow.show()
app.setWindowIcon(QIcon('LOGO.png'))


if __name__ == "__main__":
    sys.exit(app.exec_())


# def setUi(self):
#     print("Set UI")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = mainWindow()
#     sys.exit(app.exec_())
