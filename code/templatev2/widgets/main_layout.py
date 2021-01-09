# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'other_files/main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(700, 504)
        Main.setMinimumSize(QtCore.QSize(700, 500))
        Main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainBoard_widget = QtWidgets.QWidget(self.centralwidget)
        self.mainBoard_widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainBoard_widget.setToolTip("")
        self.mainBoard_widget.setStyleSheet("")
        self.mainBoard_widget.setObjectName("mainBoard_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mainBoard_widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.mainBoard_layout = QtWidgets.QVBoxLayout()
        self.mainBoard_layout.setObjectName("mainBoard_layout")
        self.verticalLayout_5.addLayout(self.mainBoard_layout)
        self.horizontalLayout.addWidget(self.mainBoard_widget)
        self.scoreBoard_widget = QtWidgets.QWidget(self.centralwidget)
        self.scoreBoard_widget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.scoreBoard_widget.setStyleSheet("")
        self.scoreBoard_widget.setObjectName("scoreBoard_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scoreBoard_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(self.scoreBoard_widget)
        self.logo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.logo.setStyleSheet("")
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.next_player_label = QtWidgets.QLabel(self.scoreBoard_widget)
        self.next_player_label.setMaximumSize(QtCore.QSize(300, 25))
        self.next_player_label.setAlignment(QtCore.Qt.AlignCenter)
        self.next_player_label.setObjectName("next_player_label")
        self.verticalLayout.addWidget(self.next_player_label)
        self.current_move_label = QtWidgets.QLabel(self.scoreBoard_widget)
        self.current_move_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.current_move_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_move_label.setObjectName("current_move_label")
        self.verticalLayout.addWidget(self.current_move_label)
        self.black_points = QtWidgets.QLabel(self.scoreBoard_widget)
        self.black_points.setAlignment(QtCore.Qt.AlignCenter)
        self.black_points.setObjectName("black_points")
        self.verticalLayout.addWidget(self.black_points)
        self.white_points = QtWidgets.QLabel(self.scoreBoard_widget)
        self.white_points.setAlignment(QtCore.Qt.AlignCenter)
        self.white_points.setObjectName("white_points")
        self.verticalLayout.addWidget(self.white_points)
        self.black_territories = QtWidgets.QLabel(self.scoreBoard_widget)
        self.black_territories.setAlignment(QtCore.Qt.AlignCenter)
        self.black_territories.setObjectName("black_territories")
        self.verticalLayout.addWidget(self.black_territories)
        self.white_territories = QtWidgets.QLabel(self.scoreBoard_widget)
        self.white_territories.setAlignment(QtCore.Qt.AlignCenter)
        self.white_territories.setObjectName("white_territories")
        self.verticalLayout.addWidget(self.white_territories)
        self.moves_count_label = QtWidgets.QLabel(self.scoreBoard_widget)
        self.moves_count_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.moves_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.moves_count_label.setObjectName("moves_count_label")
        self.verticalLayout.addWidget(self.moves_count_label)
        self.player_timer_dial = QtWidgets.QLCDNumber(self.scoreBoard_widget)
        self.player_timer_dial.setEnabled(True)
        self.player_timer_dial.setMinimumSize(QtCore.QSize(200, 50))
        self.player_timer_dial.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.player_timer_dial.setFont(font)
        self.player_timer_dial.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.player_timer_dial.setAcceptDrops(False)
        self.player_timer_dial.setMidLineWidth(0)
        self.player_timer_dial.setSmallDecimalPoint(False)
        self.player_timer_dial.setDigitCount(8)
        self.player_timer_dial.setMode(QtWidgets.QLCDNumber.Dec)
        self.player_timer_dial.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.player_timer_dial.setProperty("value", 17.885)
        self.player_timer_dial.setObjectName("player_timer_dial")
        self.verticalLayout.addWidget(self.player_timer_dial, 0, QtCore.Qt.AlignHCenter)
        self.widget = QtWidgets.QWidget(self.scoreBoard_widget)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pass_btn = QtWidgets.QPushButton(self.widget)
        self.pass_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pass_btn.setObjectName("pass_btn")
        self.gridLayout.addWidget(self.pass_btn, 0, 0, 1, 1)
        self.undo_btn = QtWidgets.QPushButton(self.widget)
        self.undo_btn.setObjectName("undo_btn")
        self.gridLayout.addWidget(self.undo_btn, 1, 0, 1, 1)
        self.reset_btn = QtWidgets.QPushButton(self.widget)
        self.reset_btn.setObjectName("reset_btn")
        self.gridLayout.addWidget(self.reset_btn, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.scoreBoard_widget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        self.help_menu = QtWidgets.QMenu(self.menubar)
        self.help_menu.setObjectName("help_menu")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.newGame_action = QtWidgets.QAction(Main)
        self.newGame_action.setObjectName("newGame_action")
        self.openGame_action = QtWidgets.QAction(Main)
        self.openGame_action.setObjectName("openGame_action")
        self.aboutGo_action = QtWidgets.QAction(Main)
        self.aboutGo_action.setObjectName("aboutGo_action")
        self.aboutGame_action = QtWidgets.QAction(Main)
        self.aboutGame_action.setObjectName("aboutGame_action")
        self.help_action = QtWidgets.QAction(Main)
        self.help_action.setObjectName("help_action")
        self.actionExit = QtWidgets.QAction(Main)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(Main)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(Main)
        self.actionHelp.setObjectName("actionHelp")
        self.file_menu.addAction(self.actionExit)
        self.help_menu.addAction(self.actionAbout)
        self.help_menu.addAction(self.actionHelp)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "AlphaGolite"))
        self.logo.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">AlphaGo</span><span style=\" font-size:20pt; vertical-align:sub;\">lite</span></p></body></html>"))
        self.next_player_label.setText(_translate("Main", " Next Player: Black"))
        self.current_move_label.setText(_translate("Main", "Coordinates: A0"))
        self.black_points.setText(_translate("Main", "Black Points: 0"))
        self.white_points.setText(_translate("Main", "White Points: 0"))
        self.black_territories.setText(_translate("Main", "Black Territories: 0"))
        self.white_territories.setText(_translate("Main", "White Territories: 0"))
        self.moves_count_label.setText(_translate("Main", "Total Moves: 0"))
        self.player_timer_dial.setToolTip(_translate("Main", "Player\'s time"))
        self.pass_btn.setText(_translate("Main", "Pass"))
        self.undo_btn.setText(_translate("Main", "Undo"))
        self.reset_btn.setText(_translate("Main", "Reset"))
        self.file_menu.setTitle(_translate("Main", "File"))
        self.help_menu.setTitle(_translate("Main", "Help"))
        self.newGame_action.setText(_translate("Main", "New Game"))
        self.newGame_action.setShortcut(_translate("Main", "Ctrl+N"))
        self.openGame_action.setText(_translate("Main", "Open Game"))
        self.openGame_action.setShortcut(_translate("Main", "Ctrl+O"))
        self.aboutGo_action.setText(_translate("Main", "About Go"))
        self.aboutGame_action.setText(_translate("Main", "About Game"))
        self.help_action.setText(_translate("Main", "Help"))
        self.actionExit.setText(_translate("Main", "Exit"))
        self.actionAbout.setText(_translate("Main", "About"))
        self.actionHelp.setText(_translate("Main", "Help"))

