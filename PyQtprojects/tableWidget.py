from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import sys
import openpyxl

class Main(QWidget):
  def __init__(self):
    super(Main, self).__init__()
    self.setWindowTitle("Loading Excel data to QTableWidget")

    layout = QVBoxLayout()
    self.setLayout(layout)

    
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = Main()
  window.showMaximized()
  app.exec_()