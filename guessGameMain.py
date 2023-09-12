from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic, QtGui
import sys, resource_rc, random
from guessGame import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.iconOnlyWidget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.loginIconOnly.setChecked(True)
        global userList
        userList = ["admin", "sample"]
        global passList
        passList = ["admin123", "sample123"]
    
        
        

    def compute1(self, guessNum, multiplier):
        answer  = int(guessNum * multiplier)
        return answer
    def compute2(self, number, rangeNumber, multiplier, multiplier2):
        if number > rangeNumber * 0.5:
            temp = rangeNumber - number
            answer = int(rangeNumber - (temp * multiplier2))
        else:
            answer = int(number * multiplier)
        return answer

    def on_profileButton_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_stackedWidget_currentChanged(self):
        btn_list = self.ui.iconOnlyWidget.findChildren(QPushButton) + self.ui.fullMenuWidget.findChildren(QPushButton) 
        for btn in btn_list:
            if self.ui.stackedWidget.currentIndex() == 3:
                 btn.setAutoExclusive(False)
                 btn.setChecked(False)
                 self.ui.profileButtonIAT.setAutoExclusive(True)
                 self.ui.profileButtonIAT.setChecked(True)
                 self.ui.profileIconOnly.setAutoExclusive(True)
                 self.ui.profileIconOnly.setChecked(True)
            elif self.ui.stackedWidget.currentIndex() == 1:
                btn.setAutoExclusive(False)
                self.ui.signupButtonIAT.setChecked(True)
            else:
                btn.setAutoExclusive(False)
            
    def on_loginIconOnly_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_loginButtonIAT_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_signupIconOnly_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_signupButtonIAT_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_playIconOnly_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def on_playButtonIAT_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_profileIconOnly_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def on_profileButtonIAT_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_login_signupButton_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_saveButton_clicked(self):
        self.ui.usernameProfile.setReadOnly(True)
        self.ui.passwordProfile.setReadOnly(True)
    def on_usernameEditButton_clicked(self):
        self.ui.usernameProfile.setReadOnly(False)
    def on_passwordEditButton_clicked(self):
        self.ui.passwordProfile.setReadOnly(False)
    
    def on_range_enterButton_pressed(self):
        global error_msg
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Warning)
        error_msg.setWindowTitle("ERROR")
        error_msg.setWindowIcon(QtGui.QIcon('icon.png'))
        if self.ui.rangeEdit.text().isdigit():
            global rangeNumber
            rangeNumber = int(self.ui.rangeEdit.text())
            if rangeNumber not in range(-2147483648, 214743648):
                error_msg.setText("Number should be between -2,147,483,648 & 2,147,483,648 only!")
                error_msg.exec_()
            else:
                global guessNum
                guessNum = random.randint(0, rangeNumber)
                self.ui.guessNumberLabel.setText("Guess the Number!")
                self.ui.guessEdit.setText("")
                self.ui.stackedWidget.setCurrentIndex(4)
                print(guessNum)
        else:
            error_msg.setText("Input should be a whole number!")
            x = error_msg.exec_()
    
    def on_resetButton_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_guessButton_pressed(self):
        print(guessNum)
        tooLow = self.compute1(guessNum, 0.2)
        higher = self.compute1(guessNum, 0.5)
        close1 = self.compute1(guessNum, 0.8)
        close2 = self.compute2(guessNum, rangeNumber, 1.2, 0.8)
        lower = self.compute2(guessNum, rangeNumber, 1.5, 0.5)
        tooHigh = self.compute2(guessNum, rangeNumber, 1.8, 0.2)
    
        if self.ui.guessEdit.text().isdigit():
            guess = int(self.ui.guessEdit.text())
            if guess not in range (0, rangeNumber + 1):
                error_msg.setText("Guess not in range!")
                a = error_msg.exec_()
            elif guess == guessNum:
                global correctGuess
                correctGuess = 0
                correctGuess += 1
                self.ui.correctGuessLabel.setText(f"Correct Guess(es): {correctGuess}")
                self.ui.guessCounterLabel.setText(f"Correct Guess(es): {correctGuess}")
                win_msg = QMessageBox()
                win_msg.setIcon(QMessageBox.Information)
                win_msg.setWindowIcon(QtGui.QIcon('icon.png'))
                win_msg.setWindowTitle("GUESS CORRECT")
                win_msg.setText("Your guess is Correct!")
                c = win_msg.exec_()
                self.ui.stackedWidget.setCurrentIndex(2)
                self.ui.rangeEdit.setText("")
            elif guess in range(close1, close2 + 1):
                self.ui.guessNumberLabel.setText("You're Close!")
            elif guess in range(tooLow, higher + 1):
                self.ui.guessNumberLabel.setText("Try Higher")
            elif guess in range(higher, close1 + 1):
                self.ui.guessNumberLabel.setText("Try Higher")
            elif guess in range(close2, lower + 1):
                self.ui.guessNumberLabel.setText("Try Lower")
            elif guess in range(lower, tooHigh + 1):
                self.ui.guessNumberLabel.setText("Try Lower")
            elif guess >= tooHigh:
                self.ui.guessNumberLabel.setText("Too High!")
            elif guess <= tooLow:
                self.ui.guessNumberLabel.setText("Too Low!")
        else:
            error_msg.setText("Input should be whole numbers only!")
            b = error_msg.exec_()

    def on_login_enterButton_pressed(self):
        error_msg2 = QMessageBox()
        error_msg2.setIcon(QMessageBox.Warning)
        error_msg2.setWindowTitle("ERROR")
        error_msg2.setWindowIcon(QtGui.QIcon('icon.png'))
        
        for i in range(0, len(userList)):
            if self.ui.usernameEdit.text() == userList[i] and self.ui.passwordEdit.text() == passList[i]:
                self.ui.stackedWidget.setCurrentIndex(2)
                self.ui.usernameProfile.setText(userList[i])
                self.ui.passwordProfile.setText(passList[i])
                break

        if self.ui.usernameEdit.text().strip() == "" and self.ui.passwordEdit.text().strip() == "":
                error_msg2.setText("Username and Password field is empty!")
                h = error_msg2.exec_()
                print("Error")
        elif self.ui.usernameEdit.text().strip() == "":
            error_msg2.setText("Username field is empty!")
            k = error_msg2.exec_()
        elif self.ui.passwordEdit.text().strip() == "":
            error_msg2.setText("Password field is empty!")
            i = error_msg2.exec_()
        elif self.ui.usernameEdit.text() not in userList and self.ui.passwordEdit.text() not in passList:
            error_msg2.setText("Invalid username or password!")
            c = error_msg2.exec_()
        

    def on_enterButton2_pressed(self):
        error_msg2 = QMessageBox()
        error_msg2.setIcon(QMessageBox.Warning)
        error_msg2.setWindowTitle("ERROR")
        error_msg2.setWindowIcon(QtGui.QIcon('icon.png'))
        if self.ui.newPasswordEdit.text() == self.ui.confirmPasswordEdit.text():
            userList.append(self.ui.newUsernameEdit.text())
            passList.append(self.ui.newPasswordEdit.text())
            print("Sucessfully added")
            self.ui.stackedWidget.setCurrentIndex(0)
        elif self.ui.newPasswordEdit.text() != self.ui.confirmPasswordEdit.text():
            error_msg2.setText("Password do not match!")
            a = error_msg2.exec_()
        else:
            error_msg2.setText("Invalid Input")
            g = error_msg2.exec_()
    
    def on_saveButton_pressed(self):
        newUsername = self.ui.usernameProfile.text()
        newPassword = self.ui.passwordProfile.text()
        for i in userList:
            userList[i] = newUsername
            passList[i] = newPassword





if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()           

    sys.exit(app.exec_())
