from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5.uic import loadUi
import sys
from PyQt5 import QtCore

class Main(QMainWindow):
  def __init__(self):
    super(Main,self).__init__()
    loadUi("C:/Users/Dell/OneDrive/Desktop/LearningPython/PyQtprojects/todo.ui", self)
    todos = ['Finish Report','Design Slide', 'Eat', 'Sleep','Drink Garri','Sleep Again']
    for todo in todos:
      item = QListWidgetItem(todo)
      item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
      item.setCheckState(QtCore.Qt.Unchecked)
      self.listWidget.addItem(item)
    self.pushButton.clicked.connect(self.toggle_all)
  def toggle_all(self):
    for i in range(self.listWidget.count()):
      item = self.listWidget.item(i)
      if item.checkState() == QtCore.Qt.Checked:
          item.setCheckState(QtCore.Qt.Unchecked)
      else:
        item.setCheckState(QtCore.Qt.Checked)
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = Main()
  window.show()
  app.exec_()