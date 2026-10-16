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
        recipient = self.lineEdit.text()
        message = self.textEdit.toPlainText()
        port = 465
        smtp_server = "smtp.gmail.com"
        sender = "a46203539@gmail.com"
        password = "nchxzbivekkprtrm"
        content = ssl.create_default_context()
        if recipient != "":
          with smtplib.SMTP_SSL(smtp_server, port, context=content) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, recipient, message)
          print("Email Sent")
        else:
          print("Email Not Sent!!!")
          tk.messagebox.showwarning("Can't send mail", "Your Recipeint email address is empty")
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = EmailSender()
  window.show()
  app.exec_()