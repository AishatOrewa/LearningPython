from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys
import smtplib, ssl
import tkinter as tk
from tkinter import messagebox
class EmailSender(QMainWindow):
  def __init__(self):
    super(EmailSender, self).__init__()
    loadUi("C:/Users/Dell/OneDrive/Desktop/LearningPython/PyQtprojects/EmailSender.ui", self)
    self.pushButton.clicked.connect(self.Send)
    def Send(self):
        print("Sending email.....")
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = EmailSender()
  window.show()
  app.exec_()