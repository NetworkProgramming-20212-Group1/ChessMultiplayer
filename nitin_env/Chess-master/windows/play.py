# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'play.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 647)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_9 = QtWidgets.QWidget(self.centralwidget)
        self.widget_9.setMinimumSize(QtCore.QSize(150, 600))
        self.widget_9.setMaximumSize(QtCore.QSize(200, 600))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.leftWidget = QtWidgets.QWidget(self.widget_9)
        self.leftWidget.setMaximumSize(QtCore.QSize(150, 600))
        self.leftWidget.setObjectName("leftWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.leftWidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius : 100; \n"
"border : 2px solid black;\n"
"padding-bottom: 5px")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.leftWidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius : 100; \n"
"border : 2px solid black;\n"
"padding-bottom: 5px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.leftWidget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius : 100; \n"
"border : 2px solid black;\n"
"padding-bottom: 5px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.leftWidget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-radius : 100; \n"
"border : 2px solid black;\n"
"padding-bottom: 5px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.widget_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.widget_7 = QtWidgets.QWidget(self.leftWidget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-radius : 100; \n"
"border : 2px solid black;\n"
"padding-bottom: 5px")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.verticalLayout.addWidget(self.widget_7)
        self.horizontalLayout_7.addWidget(self.leftWidget)
        self.widget_8 = QtWidgets.QWidget(self.widget_9)
        self.widget_8.setMinimumSize(QtCore.QSize(20, 600))
        self.widget_8.setMaximumSize(QtCore.QSize(25, 600))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.line = QtWidgets.QFrame(self.widget_8)
        self.line.setMinimumSize(QtCore.QSize(5, 600))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_8.addWidget(self.line)
        self.horizontalLayout_7.addWidget(self.widget_8)
        self.horizontalLayout_6.addWidget(self.widget_9)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(600, 600))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_22 = QtWidgets.QWidget(self.widget)
        self.widget_22.setMaximumSize(QtCore.QSize(600, 25))
        self.widget_22.setObjectName("widget_22")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_22)
        self.horizontalLayout_18.setContentsMargins(-1, 11, -1, -1)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.line_2 = QtWidgets.QFrame(self.widget_22)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_18.addWidget(self.line_2)
        self.gridLayout.addWidget(self.widget_22, 1, 0, 1, 4)
        self.widget_12 = QtWidgets.QWidget(self.widget)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_17 = QtWidgets.QWidget(self.widget_12)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.widget_17)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton_8.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("border-radius : 100; \n"
"border : 2px solid black;\n"
"padding-bottom: 5px")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_13.addWidget(self.pushButton_8)
        self.verticalLayout_3.addWidget(self.widget_17)
        self.widget_18 = QtWidgets.QWidget(self.widget_12)
        self.widget_18.setObjectName("widget_18")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_18)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_4 = QtWidgets.QLabel(self.widget_18)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_14.addWidget(self.label_4)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_18)
        self.pushButton_9.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("border-radius : 100; \n"
"border : 2px solid black;\n"
"padding-bottom: 5px")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_14.addWidget(self.pushButton_9)
        self.verticalLayout_3.addWidget(self.widget_18)
        self.widget_19 = QtWidgets.QWidget(self.widget_12)
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_5 = QtWidgets.QLabel(self.widget_19)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_15.addWidget(self.label_5)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_10.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("border-radius : 100; \n"
"border : 2px solid black;\n"
"padding-bottom: 5px")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_15.addWidget(self.pushButton_10)
        self.verticalLayout_3.addWidget(self.widget_19)
        self.widget_20 = QtWidgets.QWidget(self.widget_12)
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_6 = QtWidgets.QLabel(self.widget_20)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_16.addWidget(self.label_6)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_20)
        self.pushButton_11.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("border-radius : 100; \n"
"border : 2px solid black;\n"
"padding-bottom: 5px")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_16.addWidget(self.pushButton_11)
        self.verticalLayout_3.addWidget(self.widget_20)
        self.widget_21 = QtWidgets.QWidget(self.widget_12)
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_21)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_7 = QtWidgets.QLabel(self.widget_21)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_17.addWidget(self.label_7)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_21)
        self.pushButton_12.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("border-radius : 100; \n"
"border : 2px solid black;\n"
"padding-bottom: 5px")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_17.addWidget(self.pushButton_12)
        self.verticalLayout_3.addWidget(self.widget_21)
        self.gridLayout.addWidget(self.widget_12, 2, 3, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMaximumSize(QtCore.QSize(600, 100))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 4)
        self.widget_10 = QtWidgets.QWidget(self.widget)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_13 = QtWidgets.QWidget(self.widget_10)
        self.widget_13.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.verticalLayout_4.addWidget(self.widget_13)
        self.widget_14 = QtWidgets.QWidget(self.widget_10)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_14)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-radius : 100; \n"
"border : 2px solid black;\n"
"padding-bottom: 5px")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_10.addWidget(self.pushButton_6)
        self.verticalLayout_4.addWidget(self.widget_14)
        self.gridLayout.addWidget(self.widget_10, 2, 0, 1, 1)
        self.widget_11 = QtWidgets.QWidget(self.widget)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_15 = QtWidgets.QWidget(self.widget_11)
        self.widget_15.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.widget_15)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        self.verticalLayout_5.addWidget(self.widget_15)
        self.widget_16 = QtWidgets.QWidget(self.widget_11)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_16)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border-radius : 100; \n"
"border : 2px solid black;\n"
"padding-bottom: 5px")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_12.addWidget(self.pushButton_7)
        self.verticalLayout_5.addWidget(self.widget_16)
        self.gridLayout.addWidget(self.widget_11, 2, 1, 1, 1)
        self.widget_23 = QtWidgets.QWidget(self.widget)
        self.widget_23.setMaximumSize(QtCore.QSize(25, 16777215))
        self.widget_23.setObjectName("widget_23")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_23)
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.line_3 = QtWidgets.QFrame(self.widget_23)
        self.line_3.setMaximumSize(QtCore.QSize(25, 600))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_19.addWidget(self.line_3)
        self.gridLayout.addWidget(self.widget_23, 2, 2, 1, 1)
        self.horizontalLayout_6.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "profile"))
        self.pushButton_2.setText(_translate("MainWindow", "friends"))
        self.pushButton_3.setText(_translate("MainWindow", "group"))
        self.pushButton_4.setText(_translate("MainWindow", "play"))
        self.pushButton_5.setText(_translate("MainWindow", "Log out"))
        self.label_8.setText(_translate("MainWindow", "Room ID"))
        self.pushButton_8.setText(_translate("MainWindow", "Join"))
        self.label_4.setText(_translate("MainWindow", "Room ID"))
        self.pushButton_9.setText(_translate("MainWindow", "Join"))
        self.label_5.setText(_translate("MainWindow", "Room ID"))
        self.pushButton_10.setText(_translate("MainWindow", "Join"))
        self.label_6.setText(_translate("MainWindow", "Room ID"))
        self.pushButton_11.setText(_translate("MainWindow", "Join"))
        self.label_7.setText(_translate("MainWindow", "Room ID"))
        self.pushButton_12.setText(_translate("MainWindow", "Join"))
        self.label.setText(_translate("MainWindow", "Play"))
        self.label_2.setText(_translate("MainWindow", "Custom"))
        self.pushButton_6.setText(_translate("MainWindow", "Create Room"))
        self.label_3.setText(_translate("MainWindow", "PVP"))
        self.pushButton_7.setText(_translate("MainWindow", "Create Room"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())