from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import sys
import openpyxl

class Main(QWidget):
  def __init__(self):
    super(Main, self).__init__()
    self.setWindowTitle("Loading Excel data to QTableWidget")

    layout = QVBoxLayout()
    self.setLayout(layout)
    self.table = QTableWidget()
    layout.addWidget(self.table)
    self.load_data()
  def load_data(self):
    filepath = "C:/Users/Dell/OneDrive/Desktop/FoodiesPalace.xlsx"
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    self.table.setRowCount(sheet.max_row)
    self.table.setColumnCount(sheet.max_column)
    
    
    values = list(sheet.values)
        # self.table.setHorizontalHeader(values[0])
    self.table.setHorizontalHeaderLabels(values[0])
    row = 0
    for value in values[1:]:
      col = 0
      for val in value:
        self.table.setItem(row,col,QTableWidgetItem(str((val))))
        col +=1
      row += 1
    
    
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = Main()
  window.showMaximized()
  app.exec_()