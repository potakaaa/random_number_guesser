from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5 import uic, QtGui
import sys
import sqlite3

class signupPageUI(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("SignUp.ui", self)

        self.signupLabel = self.findChild(QLabel, "titleLabel_2")
        self.newUsername = self.findChild(QLineEdit, "newUsername")
        self.newPassword = self.findChild(QLineEdit, "newPassword")
        self.newPasswordConfirm = self.findChild(QLineEdit, "newPasswordConfirm")
        self.createAccountButton = self.findChild(QPushButton, "enterButton_2")


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #Load the ui fle
        uic.loadUi("Login.ui", self)

        #Define widgets
        self.titleLabel = self.findChild(QLabel, "titleLabel")
        self.usernameEdit = self.findChild(QLineEdit, "username")
        self.passwordEdt = self.findChild(QLineEdit, "password")
        self.signupButton = self.findChild(QPushButton, "signUpButton")
        self.enterButton = self.findChild(QPushButton, "enterButton")
        self.signupWindow = signupPageUI()


        #Actions
        self.signupButton.pressed.connect(self.signupPage)
        self.enterButton.pressed.connect(self.enter)
        
        #Show app
        self.show() 

    
    def signupPage(self):
        if self.signupWindow.isVisible():
            self.signupWindow.hide()
        else:
            self.close()
            self.signupWindow.show()
    
    def enter(self):
        username = self.usernameEdit.text()
        password = self.passwordEdt.text()
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Warning)
        errorMsg.setWindowTitle("ERROR")
        errorMsg.setWindowIcon(QtGui.QIcon('icon.png'))
        if not username.strip() and not password.strip():
            errorMsg.setText("Username and Password Field is Required!")
            a = errorMsg.exec_()
        elif not username.strip():
            errorMsg.setText("Username Field is Required!")
            b = errorMsg.exec_()
        elif not password.strip():
            errorMsg.setText("Password Field is Required!")
            c = errorMsg.exec_()
        



#Initialize app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()