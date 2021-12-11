# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(485, 276)
        MainWindow.setStyleSheet("background-color: rgb(94, 92, 100);\n"
"color: white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(50, 40, 401, 31))
        self.input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: black")
        self.input.setText("")
        self.input.setObjectName("input")
        self.btn_mp3 = QtWidgets.QRadioButton(self.centralwidget)
        self.btn_mp3.setGeometry(QtCore.QRect(10, 100, 61, 31))
        self.btn_mp3.setObjectName("btn_mp3")
        self.btn_mp4 = QtWidgets.QRadioButton(self.centralwidget)
        self.btn_mp4.setGeometry(QtCore.QRect(280, 100, 92, 25))
        self.btn_mp4.setObjectName("btn_mp4")
        self.btn_playlist_mp3 = QtWidgets.QRadioButton(self.centralwidget)
        self.btn_playlist_mp3.setGeometry(QtCore.QRect(110, 100, 111, 25))
        self.btn_playlist_mp3.setObjectName("btn_playlist_mp3")
        self.download_btn = QtWidgets.QPushButton(self.centralwidget)
        self.download_btn.setGeometry(QtCore.QRect(110, 170, 241, 51))
        self.download_btn.setStyleSheet("background-color: rgb(53, 132, 228);\n"
"border-radius: 10px;\n"
"color: white")
        self.download_btn.setObjectName("download_btn")
        self.btn_playlist_mp4 = QtWidgets.QRadioButton(self.centralwidget)
        self.btn_playlist_mp4.setGeometry(QtCore.QRect(370, 100, 111, 25))
        self.btn_playlist_mp4.setObjectName("btn_playlist_mp4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 31, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_mp3.setText(_translate("MainWindow", "MP3"))
        self.btn_mp4.setText(_translate("MainWindow", "MP4"))
        self.btn_playlist_mp3.setText(_translate("MainWindow", "Playlist MP3"))
        self.download_btn.setText(_translate("MainWindow", "Start Downlaod"))
        self.btn_playlist_mp4.setText(_translate("MainWindow", "Playlist MP4"))
        self.label.setText(_translate("MainWindow", "URL"))