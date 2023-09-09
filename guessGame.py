# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\guessGame.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 835)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#iconOnlyWidget, #iconTextWidget {\n"
"background-color: qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"}\n"
"\n"
"#iconOnlyWidget {\n"
"width: 50px;\n"
"}\n"
"\n"
"#logoIconOnly {\n"
"padding: 5px;\n"
"}\n"
"\n"
"#logoIAT {\n"
"padding: 4px;\n"
"}\n"
"\n"
"#iconOnlyWidget QPushButton{\n"
"color: rgb(67, 67, 67);\n"
"border: none;\n"
"height: 50px;\n"
"color: white;\n"
"margin: 5px;\n"
"padding: 5px;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"#iconOnlyWidget QPushButton::hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"}\n"
"\n"
"\n"
"#iconTextWidget QPushButton{\n"
"border: none;\n"
"height: 50px;\n"
"color: black;\n"
"margin: 5px;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#iconTextWidget QPushButton::hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"color: white;\n"
"}\n"
"\n"
"#iconTextWidget QPushButton {\n"
"font: 14px \"Alegreya Sans SC\";\n"
"}\n"
"\n"
"#fullMenuWidget {\n"
"background-color: qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ECE9E6, stop:1 #FFFFFF);\n"
"}\n"
"\n"
"#header QPushButton {\n"
"border: none;\n"
"padding: 8px;\n"
"border-radius: 10px;\n"
"margin: 5px;\n"
"}\n"
"\n"
"#header QPushButton::hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"}\n"
"\n"
"#stackedWidget {\n"
"text-align: left;\n"
"background-color: #330033;\n"
"}\n"
"\n"
"#iconOnlyWidget #exitIconOnly {\n"
"padding: 15px;\n"
"}\n"
"\n"
"#loginPage #loginpageLabel {\n"
"font-weight: bold;\n"
"font-size: 45px;\n"
"font-family: \"Alegreya Sans SC\";\n"
"margin: 0;\n"
"padding: 0;\n"
"color: #ffa500;\n"
"}\n"
"\n"
"#loginPage #usernameLabel, #passwordLabel {\n"
"font-size: 20px;\n"
"font-family: \"Alegreya Sans SC\";\n"
"margin: 10px 40px 10px;\n"
"color: #ffa500;\n"
"}\n"
"\n"
"#loginPage QLineEdit {\n"
"height: 40px;\n"
"border-radius: 17px;\n"
"border: 2px solid black;\n"
"margin: 10px 40px 10px;\n"
"padding: 10px;\n"
"font-size: 15px;\n"
"}\n"
"#loginPage QLineEdit::focus {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"}\n"
"\n"
"#loginPage QPushButton {\n"
"height: 50px;\n"
"font-size: 18px;\n"
"font-family: \"Alegreya Sans SC\";\n"
"margin: 10px 50px 10px;\n"
"border: none;\n"
"color: #ffa500;\n"
"}\n"
"\n"
"#loginPage QPushButton::hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"color: black;\n"
"}\n"
"\n"
"#signupPage #signuppageLabel {\n"
"font-weight: bold;\n"
"font-size: 45px;\n"
"font-family: \"Alegreya Sans SC\";\n"
"margin: 0;\n"
"padding: 0;\n"
"color: #ffa500;\n"
"}\n"
"\n"
"#signupPage #newUsernameLabel, #newPasswordLabel, #confirmPasswordLabel {\n"
"font-size: 20px;\n"
"font-family: \"Alegreya Sans SC\";\n"
"margin: 10px 40px 10px;\n"
"color: #ffa500;\n"
"}\n"
"\n"
"#signupPage QLineEdit {\n"
"height: 40px;\n"
"border-radius: 17px;\n"
"border: 2px solid black;\n"
"margin: 10px 40px 10px;\n"
"padding: 10px;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"#signupPage QLineEdit::focus {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"}\n"
"\n"
"#signupPage QPushButton {\n"
"height: 50px;\n"
"font-size: 18px;\n"
"font-family: \"Alegreya Sans SC\";\n"
"margin: 10px 50px 10px;\n"
"border: none;\n"
"color: #ffa500;\n"
"}\n"
"\n"
"#signupPage QPushButton::hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"color: black;\n"
"}\n"
"\n"
"#rangePage QLabel {\n"
"margin: 10px;\n"
"padding: 0;\n"
"color: #ffa500;\n"
"}\n"
"\n"
"#rangePage QPushButton {\n"
"height: 50px;\n"
"font-size: 18px;\n"
"font-family: \"Alegreya Sans SC\";\n"
"margin: 10px 50px 10px;\n"
"border: none;\n"
"color: #ffa500;\n"
"}\n"
"\n"
"#rangePage QPushButton::hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"color: black;\n"
"}\n"
"\n"
"#rangePage QLineEdit {\n"
"height: 40px;\n"
"border-radius: 17px;\n"
"border: 2px solid black;\n"
"margin: 20px 40px 10px;\n"
"padding: 10px;\n"
"font-size: 30px;\n"
"font-family: \"Terminal\";\n"
"text-align: center;\n"
"}\n"
"\n"
"#profilePage QLineEdit::focus {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"}\n"
"\n"
"#rangePage QLineEdit::focus {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"}\n"
"\n"
"#profilePage #profilePicture {\n"
"margin: 0px 10px 0px;\n"
"\n"
"border-radius: 50%\n"
"}\n"
"\n"
"#profilePage QLineEdit {\n"
"height: 18px;\n"
"width: 250px;\n"
"border-radius: 17px;\n"
"border: 2px solid black;\n"
"margin: 3px;\n"
"padding: 10px;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"#profilePage #saveButton {\n"
"margin: 5px 50px 5px;\n"
"height: 40px;\n"
"font-size: 18px;\n"
"font-family: \"Alegreya Sans SC\";\n"
"margin-left: 15px;\n"
"border: none;\n"
"color: #ffa500;\n"
"}\n"
"\n"
"#profilePage #saveButton::hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"color: black;\n"
"}\n"
"\n"
"#profilePage #usernameEditButton, #passwordEditButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"border-radius: 5px;\n"
"width: 30px;\n"
"height: 30px;\n"
"}\n"
"\n"
"#profilePage #usernameEditButton::hover, #passwordEditButton::hover {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"background-color: white;\n"
"}\n"
"\n"
"#profilePage #guessCounterLabel {\n"
"color: white;\n"
"margin: 5px 5px 5px;\n"
"}\n"
"\n"
"#playPage #guessNumberLabel {\n"
"margin: 0px 10px 30px;\n"
"padding: 0;\n"
"color: #ffa500;\n"
"}\n"
"\n"
"#playPage #guessEdit {\n"
"height: 40px;\n"
"border-radius: 17px;\n"
"border: 2px solid black;\n"
"margin: 0px 40px 10px;\n"
"padding: 10px;\n"
"font-size: 30px;\n"
"font-family: \"Terminal\";\n"
"text-align: center;\n"
"}\n"
"\n"
"#playPage #guessEdit::focus {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"}\n"
"\n"
"#playPage QPushButton {\n"
"height: 50px;\n"
"font-size: 22px;\n"
"font-family: \"Alegreya Sans SC\";\n"
"margin: 10px 20px 10px;\n"
"border: none;\n"
"color: #ffa500;\n"
"}\n"
"\n"
"#playPage QPushButton::hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.488636, y2:1, stop:0 #ffb347, stop:1 #ffcc33);\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"color: black;\n"
"}\n"
"\n"
"#playPage #correctGuessLabel {\n"
"color:white;\n"
"margin: 15px 0px 0px\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.iconOnlyWidget = QtWidgets.QWidget(self.centralwidget)
        self.iconOnlyWidget.setObjectName("iconOnlyWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.iconOnlyWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 9, -1, 6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logoIconOnly = QtWidgets.QLabel(self.iconOnlyWidget)
        self.logoIconOnly.setMinimumSize(QtCore.QSize(50, 50))
        self.logoIconOnly.setMaximumSize(QtCore.QSize(50, 50))
        self.logoIconOnly.setText("")
        self.logoIconOnly.setPixmap(QtGui.QPixmap(":/icons/icons/71jgOh9AaBL.png"))
        self.logoIconOnly.setScaledContents(True)
        self.logoIconOnly.setObjectName("logoIconOnly")
        self.horizontalLayout_2.addWidget(self.logoIconOnly)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginIconOnly = QtWidgets.QPushButton(self.iconOnlyWidget)
        self.loginIconOnly.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginIconOnly.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/log-in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/log-in_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.loginIconOnly.setIcon(icon1)
        self.loginIconOnly.setIconSize(QtCore.QSize(20, 20))
        self.loginIconOnly.setCheckable(True)
        self.loginIconOnly.setAutoExclusive(True)
        self.loginIconOnly.setObjectName("loginIconOnly")
        self.verticalLayout.addWidget(self.loginIconOnly)
        self.signupIconOnly = QtWidgets.QPushButton(self.iconOnlyWidget)
        self.signupIconOnly.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupIconOnly.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/user-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/user-plus_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.signupIconOnly.setIcon(icon2)
        self.signupIconOnly.setIconSize(QtCore.QSize(20, 20))
        self.signupIconOnly.setCheckable(True)
        self.signupIconOnly.setAutoExclusive(True)
        self.signupIconOnly.setObjectName("signupIconOnly")
        self.verticalLayout.addWidget(self.signupIconOnly)
        self.playIconOnly = QtWidgets.QPushButton(self.iconOnlyWidget)
        self.playIconOnly.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playIconOnly.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/play_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.playIconOnly.setIcon(icon3)
        self.playIconOnly.setIconSize(QtCore.QSize(20, 20))
        self.playIconOnly.setCheckable(True)
        self.playIconOnly.setAutoExclusive(True)
        self.playIconOnly.setObjectName("playIconOnly")
        self.verticalLayout.addWidget(self.playIconOnly)
        self.profileIconOnly = QtWidgets.QPushButton(self.iconOnlyWidget)
        self.profileIconOnly.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profileIconOnly.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/user_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.profileIconOnly.setIcon(icon4)
        self.profileIconOnly.setIconSize(QtCore.QSize(20, 20))
        self.profileIconOnly.setCheckable(True)
        self.profileIconOnly.setAutoExclusive(True)
        self.profileIconOnly.setObjectName("profileIconOnly")
        self.verticalLayout.addWidget(self.profileIconOnly)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 638, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.exitIconOnly = QtWidgets.QPushButton(self.iconOnlyWidget)
        self.exitIconOnly.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitIconOnly.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitIconOnly.setIcon(icon5)
        self.exitIconOnly.setIconSize(QtCore.QSize(20, 20))
        self.exitIconOnly.setObjectName("exitIconOnly")
        self.verticalLayout_2.addWidget(self.exitIconOnly)
        self.gridLayout.addWidget(self.iconOnlyWidget, 0, 0, 1, 1)
        self.iconTextWidget = QtWidgets.QWidget(self.centralwidget)
        self.iconTextWidget.setObjectName("iconTextWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.iconTextWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logoIAT = QtWidgets.QLabel(self.iconTextWidget)
        self.logoIAT.setMinimumSize(QtCore.QSize(40, 40))
        self.logoIAT.setMaximumSize(QtCore.QSize(40, 40))
        self.logoIAT.setText("")
        self.logoIAT.setPixmap(QtGui.QPixmap(":/icons/icons/71jgOh9AaBL.png"))
        self.logoIAT.setScaledContents(True)
        self.logoIAT.setObjectName("logoIAT")
        self.horizontalLayout.addWidget(self.logoIAT)
        self.guessGameLabel = QtWidgets.QLabel(self.iconTextWidget)
        font = QtGui.QFont()
        font.setFamily("Alegreya Sans SC")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.guessGameLabel.setFont(font)
        self.guessGameLabel.setObjectName("guessGameLabel")
        self.horizontalLayout.addWidget(self.guessGameLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.loginButtonIAT = QtWidgets.QPushButton(self.iconTextWidget)
        self.loginButtonIAT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButtonIAT.setIcon(icon1)
        self.loginButtonIAT.setIconSize(QtCore.QSize(14, 14))
        self.loginButtonIAT.setCheckable(True)
        self.loginButtonIAT.setAutoExclusive(True)
        self.loginButtonIAT.setObjectName("loginButtonIAT")
        self.verticalLayout_3.addWidget(self.loginButtonIAT)
        self.signupButtonIAT = QtWidgets.QPushButton(self.iconTextWidget)
        self.signupButtonIAT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupButtonIAT.setIcon(icon2)
        self.signupButtonIAT.setIconSize(QtCore.QSize(14, 14))
        self.signupButtonIAT.setCheckable(True)
        self.signupButtonIAT.setAutoExclusive(True)
        self.signupButtonIAT.setObjectName("signupButtonIAT")
        self.verticalLayout_3.addWidget(self.signupButtonIAT)
        self.playButtonIAT = QtWidgets.QPushButton(self.iconTextWidget)
        self.playButtonIAT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playButtonIAT.setIcon(icon3)
        self.playButtonIAT.setIconSize(QtCore.QSize(14, 14))
        self.playButtonIAT.setCheckable(True)
        self.playButtonIAT.setAutoExclusive(True)
        self.playButtonIAT.setObjectName("playButtonIAT")
        self.verticalLayout_3.addWidget(self.playButtonIAT)
        self.profileButtonIAT = QtWidgets.QPushButton(self.iconTextWidget)
        self.profileButtonIAT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profileButtonIAT.setIcon(icon4)
        self.profileButtonIAT.setIconSize(QtCore.QSize(14, 14))
        self.profileButtonIAT.setCheckable(True)
        self.profileButtonIAT.setAutoExclusive(True)
        self.profileButtonIAT.setObjectName("profileButtonIAT")
        self.verticalLayout_3.addWidget(self.profileButtonIAT)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 637, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.exitButtonIAT = QtWidgets.QPushButton(self.iconTextWidget)
        self.exitButtonIAT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButtonIAT.setIcon(icon5)
        self.exitButtonIAT.setIconSize(QtCore.QSize(14, 14))
        self.exitButtonIAT.setObjectName("exitButtonIAT")
        self.verticalLayout_4.addWidget(self.exitButtonIAT)
        self.gridLayout.addWidget(self.iconTextWidget, 0, 1, 1, 1)
        self.fullMenuWidget = QtWidgets.QWidget(self.centralwidget)
        self.fullMenuWidget.setObjectName("fullMenuWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fullMenuWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.header = QtWidgets.QWidget(self.fullMenuWidget)
        self.header.setMinimumSize(QtCore.QSize(0, 60))
        self.header.setObjectName("header")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menuButton = QtWidgets.QPushButton(self.header)
        self.menuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon6)
        self.menuButton.setIconSize(QtCore.QSize(20, 20))
        self.menuButton.setCheckable(True)
        self.menuButton.setObjectName("menuButton")
        self.horizontalLayout_3.addWidget(self.menuButton)
        spacerItem2 = QtWidgets.QSpacerItem(287, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.randomGuesserLabel = QtWidgets.QLabel(self.header)
        font = QtGui.QFont()
        font.setFamily("Alegreya Sans SC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.randomGuesserLabel.setFont(font)
        self.randomGuesserLabel.setObjectName("randomGuesserLabel")
        self.horizontalLayout_3.addWidget(self.randomGuesserLabel)
        spacerItem3 = QtWidgets.QSpacerItem(286, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.profileButton = QtWidgets.QPushButton(self.header)
        self.profileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profileButton.setText("")
        self.profileButton.setIcon(icon4)
        self.profileButton.setIconSize(QtCore.QSize(20, 20))
        self.profileButton.setCheckable(False)
        self.profileButton.setAutoExclusive(False)
        self.profileButton.setObjectName("profileButton")
        self.horizontalLayout_3.addWidget(self.profileButton)
        self.verticalLayout_5.addWidget(self.header)
        self.stackedWidget = QtWidgets.QStackedWidget(self.fullMenuWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.loginPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 5, 0, 1, 1)
        self.loginpageLabel = QtWidgets.QLabel(self.loginPage)
        self.loginpageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginpageLabel.setObjectName("loginpageLabel")
        self.gridLayout_2.addWidget(self.loginpageLabel, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.usernameLabel = QtWidgets.QLabel(self.loginPage)
        self.usernameLabel.setObjectName("usernameLabel")
        self.verticalLayout_6.addWidget(self.usernameLabel)
        self.usernameEdit = QtWidgets.QLineEdit(self.loginPage)
        self.usernameEdit.setObjectName("usernameEdit")
        self.verticalLayout_6.addWidget(self.usernameEdit)
        self.passwordLabel = QtWidgets.QLabel(self.loginPage)
        self.passwordLabel.setObjectName("passwordLabel")
        self.verticalLayout_6.addWidget(self.passwordLabel)
        self.passwordEdit = QtWidgets.QLineEdit(self.loginPage)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.verticalLayout_6.addWidget(self.passwordEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.login_signupButton = QtWidgets.QPushButton(self.loginPage)
        self.login_signupButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_signupButton.setCheckable(True)
        self.login_signupButton.setAutoExclusive(True)
        self.login_signupButton.setObjectName("login_signupButton")
        self.horizontalLayout_4.addWidget(self.login_signupButton)
        self.login_enterButton = QtWidgets.QPushButton(self.loginPage)
        self.login_enterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_enterButton.setObjectName("login_enterButton")
        self.horizontalLayout_4.addWidget(self.login_enterButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.loginPage)
        self.signupPage = QtWidgets.QWidget()
        self.signupPage.setObjectName("signupPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.signupPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.signuppageLabel = QtWidgets.QLabel(self.signupPage)
        self.signuppageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.signuppageLabel.setObjectName("signuppageLabel")
        self.gridLayout_3.addWidget(self.signuppageLabel, 1, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.newUsernameLabel = QtWidgets.QLabel(self.signupPage)
        self.newUsernameLabel.setObjectName("newUsernameLabel")
        self.verticalLayout_7.addWidget(self.newUsernameLabel)
        self.newUsernameEdit = QtWidgets.QLineEdit(self.signupPage)
        self.newUsernameEdit.setObjectName("newUsernameEdit")
        self.verticalLayout_7.addWidget(self.newUsernameEdit)
        self.newPasswordLabel = QtWidgets.QLabel(self.signupPage)
        self.newPasswordLabel.setObjectName("newPasswordLabel")
        self.verticalLayout_7.addWidget(self.newPasswordLabel)
        self.newPasswordEdit = QtWidgets.QLineEdit(self.signupPage)
        self.newPasswordEdit.setObjectName("newPasswordEdit")
        self.verticalLayout_7.addWidget(self.newPasswordEdit)
        self.confirmPasswordLabel = QtWidgets.QLabel(self.signupPage)
        self.confirmPasswordLabel.setObjectName("confirmPasswordLabel")
        self.verticalLayout_7.addWidget(self.confirmPasswordLabel)
        self.confirmPasswordEdit = QtWidgets.QLineEdit(self.signupPage)
        self.confirmPasswordEdit.setObjectName("confirmPasswordEdit")
        self.verticalLayout_7.addWidget(self.confirmPasswordEdit)
        self.enterButton2 = QtWidgets.QPushButton(self.signupPage)
        self.enterButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterButton2.setObjectName("enterButton2")
        self.verticalLayout_7.addWidget(self.enterButton2)
        self.gridLayout_3.addLayout(self.verticalLayout_7, 3, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem7, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 2, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 4, 0, 1, 1)
        self.stackedWidget.addWidget(self.signupPage)
        self.rangePage = QtWidgets.QWidget()
        self.rangePage.setObjectName("rangePage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.rangePage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 2, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.rangeEdit = QtWidgets.QLineEdit(self.rangePage)
        self.rangeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.rangeEdit.setObjectName("rangeEdit")
        self.verticalLayout_8.addWidget(self.rangeEdit)
        self.range_enterButton = QtWidgets.QPushButton(self.rangePage)
        self.range_enterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.range_enterButton.setObjectName("range_enterButton")
        self.verticalLayout_8.addWidget(self.range_enterButton)
        self.gridLayout_4.addLayout(self.verticalLayout_8, 2, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem11, 0, 1, 1, 1)
        self.rangeLabel = QtWidgets.QLabel(self.rangePage)
        font = QtGui.QFont()
        font.setFamily("Alegreya Sans SC")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.rangeLabel.setFont(font)
        self.rangeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rangeLabel.setObjectName("rangeLabel")
        self.gridLayout_4.addWidget(self.rangeLabel, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 2, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem13, 3, 1, 1, 1)
        self.stackedWidget.addWidget(self.rangePage)
        self.profilePage = QtWidgets.QWidget()
        self.profilePage.setObjectName("profilePage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.profilePage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem14, 0, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem15, 1, 0, 1, 1)
        self.profilePicture = QtWidgets.QLabel(self.profilePage)
        self.profilePicture.setMaximumSize(QtCore.QSize(210, 210))
        self.profilePicture.setText("")
        self.profilePicture.setPixmap(QtGui.QPixmap(":/icons/icons/189533.png"))
        self.profilePicture.setScaledContents(False)
        self.profilePicture.setAlignment(QtCore.Qt.AlignCenter)
        self.profilePicture.setObjectName("profilePicture")
        self.gridLayout_5.addWidget(self.profilePicture, 1, 1, 4, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.usernameProfile = QtWidgets.QLineEdit(self.profilePage)
        self.usernameProfile.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.usernameProfile.setReadOnly(True)
        self.usernameProfile.setObjectName("usernameProfile")
        self.horizontalLayout_5.addWidget(self.usernameProfile)
        self.usernameEditButton = QtWidgets.QPushButton(self.profilePage)
        self.usernameEditButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.usernameEditButton.setIcon(icon7)
        self.usernameEditButton.setObjectName("usernameEditButton")
        self.horizontalLayout_5.addWidget(self.usernameEditButton)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem16, 1, 3, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.passwordProfile = QtWidgets.QLineEdit(self.profilePage)
        self.passwordProfile.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passwordProfile.setReadOnly(True)
        self.passwordProfile.setObjectName("passwordProfile")
        self.horizontalLayout_6.addWidget(self.passwordProfile)
        self.passwordEditButton = QtWidgets.QPushButton(self.profilePage)
        self.passwordEditButton.setText("")
        self.passwordEditButton.setIcon(icon7)
        self.passwordEditButton.setObjectName("passwordEditButton")
        self.horizontalLayout_6.addWidget(self.passwordEditButton)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 2, 2, 1, 1)
        self.guessCounterLabel = QtWidgets.QLabel(self.profilePage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.guessCounterLabel.setFont(font)
        self.guessCounterLabel.setObjectName("guessCounterLabel")
        self.gridLayout_5.addWidget(self.guessCounterLabel, 3, 2, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.profilePage)
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_5.addWidget(self.saveButton, 4, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem17, 5, 2, 1, 1)
        self.stackedWidget.addWidget(self.profilePage)
        self.playPage = QtWidgets.QWidget()
        self.playPage.setObjectName("playPage")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.playPage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.guessEdit = QtWidgets.QLineEdit(self.playPage)
        self.guessEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.guessEdit.setObjectName("guessEdit")
        self.verticalLayout_9.addWidget(self.guessEdit)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.resetButton = QtWidgets.QPushButton(self.playPage)
        self.resetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_7.addWidget(self.resetButton)
        self.guessButton = QtWidgets.QPushButton(self.playPage)
        self.guessButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.guessButton.setObjectName("guessButton")
        self.horizontalLayout_7.addWidget(self.guessButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.correctGuessLabel = QtWidgets.QLabel(self.playPage)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.correctGuessLabel.setFont(font)
        self.correctGuessLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.correctGuessLabel.setObjectName("correctGuessLabel")
        self.verticalLayout_9.addWidget(self.correctGuessLabel)
        self.gridLayout_6.addLayout(self.verticalLayout_9, 2, 1, 1, 1)
        self.guessNumberLabel = QtWidgets.QLabel(self.playPage)
        font = QtGui.QFont()
        font.setFamily("Alegreya Sans SC")
        font.setPointSize(40)
        self.guessNumberLabel.setFont(font)
        self.guessNumberLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.guessNumberLabel.setObjectName("guessNumberLabel")
        self.gridLayout_6.addWidget(self.guessNumberLabel, 1, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem18, 0, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem19, 1, 2, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem20, 3, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem21, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.playPage)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.fullMenuWidget, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.menuButton.toggled['bool'].connect(self.iconOnlyWidget.setVisible) # type: ignore
        self.menuButton.toggled['bool'].connect(self.iconTextWidget.setHidden) # type: ignore
        self.loginIconOnly.toggled['bool'].connect(self.loginButtonIAT.setChecked) # type: ignore
        self.signupIconOnly.toggled['bool'].connect(self.signupButtonIAT.setChecked) # type: ignore
        self.playIconOnly.toggled['bool'].connect(self.playButtonIAT.setChecked) # type: ignore
        self.profileIconOnly.toggled['bool'].connect(self.profileButtonIAT.setChecked) # type: ignore
        self.loginButtonIAT.toggled['bool'].connect(self.loginIconOnly.setChecked) # type: ignore
        self.signupButtonIAT.toggled['bool'].connect(self.signupIconOnly.setChecked) # type: ignore
        self.playButtonIAT.toggled['bool'].connect(self.playIconOnly.setChecked) # type: ignore
        self.profileButtonIAT.toggled['bool'].connect(self.profileIconOnly.setChecked) # type: ignore
        self.exitButtonIAT.clicked.connect(MainWindow.close) # type: ignore
        self.exitIconOnly.clicked.connect(MainWindow.close) # type: ignore
        self.login_signupButton.toggled['bool'].connect(self.signupButtonIAT.setChecked) # type: ignore
        self.login_signupButton.toggled['bool'].connect(self.signupIconOnly.setChecked) # type: ignore
        self.profileIconOnly.toggled['bool'].connect(self.profileButton.setChecked) # type: ignore
        self.profileButtonIAT.toggled['bool'].connect(self.profileButton.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.guessGameLabel.setText(_translate("MainWindow", "<html><head/><body><p>Guess Game</p></body></html>"))
        self.loginButtonIAT.setText(_translate("MainWindow", "Login"))
        self.signupButtonIAT.setText(_translate("MainWindow", "Sign Up"))
        self.playButtonIAT.setText(_translate("MainWindow", "Play"))
        self.profileButtonIAT.setText(_translate("MainWindow", "Profile"))
        self.exitButtonIAT.setText(_translate("MainWindow", "Exit"))
        self.randomGuesserLabel.setText(_translate("MainWindow", "Random Number Guesser"))
        self.loginpageLabel.setText(_translate("MainWindow", "LOG IN"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.login_signupButton.setText(_translate("MainWindow", "Sign Up"))
        self.login_enterButton.setText(_translate("MainWindow", "Enter"))
        self.signuppageLabel.setText(_translate("MainWindow", "SIGN UP"))
        self.newUsernameLabel.setText(_translate("MainWindow", "Username"))
        self.newPasswordLabel.setText(_translate("MainWindow", "Password"))
        self.confirmPasswordLabel.setText(_translate("MainWindow", "Confirm Password"))
        self.enterButton2.setText(_translate("MainWindow", "Enter"))
        self.range_enterButton.setText(_translate("MainWindow", "ENTER"))
        self.rangeLabel.setText(_translate("MainWindow", "Input range to guess"))
        self.usernameProfile.setPlaceholderText(_translate("MainWindow", "Username"))
        self.passwordProfile.setPlaceholderText(_translate("MainWindow", "Password"))
        self.guessCounterLabel.setText(_translate("MainWindow", "Correct Guess(es): 0"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.guessButton.setText(_translate("MainWindow", "Guess"))
        self.correctGuessLabel.setText(_translate("MainWindow", "Correct Guess(es): 0"))
        self.guessNumberLabel.setText(_translate("MainWindow", "Guess the Number!"))
import resource_rc
