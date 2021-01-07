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
        self.status_box = QtWidgets.QWidget(self.scoreBoard_widget)
        self.status_box.setMaximumSize(QtCore.QSize(300, 50))
        self.status_box.setObjectName("status_box")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.status_box)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.moves_count_label = QtWidgets.QLabel(self.status_box)
        self.moves_count_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.moves_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.moves_count_label.setObjectName("moves_count_label")
        self.horizontalLayout_6.addWidget(self.moves_count_label)
        self.current_move_label = QtWidgets.QLabel(self.status_box)
        self.current_move_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.current_move_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_move_label.setObjectName("current_move_label")
        self.horizontalLayout_6.addWidget(self.current_move_label)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.status_box)
        self.widget_4 = QtWidgets.QWidget(self.scoreBoard_widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 10, 201, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.current_player_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.current_player_label.setMaximumSize(QtCore.QSize(300, 25))
        self.current_player_label.setObjectName("current_player_label")
        self.horizontalLayout_3.addWidget(self.current_player_label)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.scoreBoard_widget)
        self.widget_3.setEnabled(True)
        self.widget_3.setMaximumSize(QtCore.QSize(300, 50))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.points_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.points_label.setMaximumSize(QtCore.QSize(300, 25))
        self.points_label.setObjectName("points_label")
        self.horizontalLayout_5.addWidget(self.points_label)
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setGeometry(QtCore.QRect(10, 50, 191, 31))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout.addWidget(self.widget_3)
        self.player_timer_dial = QtWidgets.QLCDNumber(self.scoreBoard_widget)
        self.player_timer_dial.setEnabled(True)
        self.player_timer_dial.setMaximumSize(QtCore.QSize(16777215, 50))
        self.player_timer_dial.setAcceptDrops(False)
        self.player_timer_dial.setMidLineWidth(0)
        self.player_timer_dial.setSmallDecimalPoint(False)
        self.player_timer_dial.setDigitCount(8)
        self.player_timer_dial.setMode(QtWidgets.QLCDNumber.Dec)
        self.player_timer_dial.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.player_timer_dial.setProperty("value", 17.885)
        self.player_timer_dial.setObjectName("player_timer_dial")
        self.verticalLayout.addWidget(self.player_timer_dial)
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
        self.saveGame_action = QtWidgets.QAction(Main)
        self.saveGame_action.setObjectName("saveGame_action")
        self.aboutGo_action = QtWidgets.QAction(Main)
        self.aboutGo_action.setObjectName("aboutGo_action")
        self.aboutGame_action = QtWidgets.QAction(Main)
        self.aboutGame_action.setObjectName("aboutGame_action")
        self.help_action = QtWidgets.QAction(Main)
        self.help_action.setObjectName("help_action")
        self.file_menu.addAction(self.newGame_action)
        self.file_menu.addAction(self.openGame_action)
        self.file_menu.addAction(self.saveGame_action)
        self.help_menu.addAction(self.aboutGo_action)
        self.help_menu.addAction(self.aboutGame_action)
        self.help_menu.addAction(self.help_action)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "AlphaGolite"))
        self.logo.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">AlphaGo</span><span style=\" font-size:20pt; vertical-align:sub;\">lite</span></p></body></html>"))
        self.moves_count_label.setText(_translate("Main", "Moves: 30"))
        self.current_move_label.setText(_translate("Main", "White: 3J"))
        self.current_player_label.setText(_translate("Main", " Player:"))
        self.points_label.setText(_translate("Main", " Points: "))
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
        self.saveGame_action.setText(_translate("Main", "Save Game"))
        self.saveGame_action.setShortcut(_translate("Main", "Ctrl+S"))
        self.aboutGo_action.setText(_translate("Main", "About Go"))
        self.aboutGame_action.setText(_translate("Main", "About Game"))
        self.help_action.setText(_translate("Main", "Help"))

