# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1280, 800)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../.designer/Images/EPA1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1278, 723))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabInner = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabInner.setEnabled(True)
        self.tabInner.setObjectName("tabInner")
        self.tabSubcatchments = QtWidgets.QWidget()
        self.tabSubcatchments.setObjectName("tabSubcatchments")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabSubcatchments)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget = QtWidgets.QWidget(self.tabSubcatchments)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listSubcatchments = QtWidgets.QListWidget(self.widget)
        self.listSubcatchments.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listSubcatchments.setObjectName("listSubcatchments")
        self.gridLayout_3.addWidget(self.listSubcatchments, 0, 0, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.widget)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 948, 591))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout_Sub = QtWidgets.QFormLayout()
        self.formLayout_Sub.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_Sub.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_Sub.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout_Sub.setContentsMargins(50, 10, 50, 10)
        self.formLayout_Sub.setHorizontalSpacing(10)
        self.formLayout_Sub.setVerticalSpacing(12)
        self.formLayout_Sub.setObjectName("formLayout_Sub")
        self.gridLayout_4.addLayout(self.formLayout_Sub, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.widget)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.tabInner.addTab(self.tabSubcatchments, "")
        self.tabLID_Controls = QtWidgets.QWidget()
        self.tabLID_Controls.setObjectName("tabLID_Controls")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tabLID_Controls)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.tabLID_Controls)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.listLID_Controls = QtWidgets.QListWidget(self.widget_2)
        self.listLID_Controls.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listLID_Controls.setObjectName("listLID_Controls")
        self.gridLayout_6.addWidget(self.listLID_Controls, 0, 0, 1, 1)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.widget_2)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 948, 591))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.formLayout_LID = QtWidgets.QFormLayout()
        self.formLayout_LID.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout_LID.setContentsMargins(50, 10, 50, 10)
        self.formLayout_LID.setHorizontalSpacing(10)
        self.formLayout_LID.setVerticalSpacing(12)
        self.formLayout_LID.setObjectName("formLayout_LID")
        self.gridLayout_7.addLayout(self.formLayout_LID, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_6.addWidget(self.scrollArea_3, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_5)
        self.tabInner.addTab(self.tabLID_Controls, "")
        self.gridLayout_2.addWidget(self.tabInner, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 38))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionRun_Pest_Calibration = QtWidgets.QAction(MainWindow)
        self.actionRun_Pest_Calibration.setObjectName("actionRun_Pest_Calibration")
        self.actionTest = QtWidgets.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionGuide = QtWidgets.QAction(MainWindow)
        self.actionGuide.setObjectName("actionGuide")
        self.actionPyQt = QtWidgets.QAction(MainWindow)
        self.actionPyQt.setObjectName("actionPyQt")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menuRun.addAction(self.actionRun_Pest_Calibration)
        self.menuHelp.addAction(self.actionGuide)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabInner.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SWMM2PEST"))
        self.tabInner.setTabText(self.tabInner.indexOf(self.tabSubcatchments), _translate("MainWindow", "Subcatchments"))
        self.tabInner.setTabText(self.tabInner.indexOf(self.tabLID_Controls), _translate("MainWindow", "LID_Controls"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionRun_Pest_Calibration.setText(_translate("MainWindow", "Run Pest Calibration"))
        self.actionTest.setText(_translate("MainWindow", "Test"))
        self.actionGuide.setText(_translate("MainWindow", "Guide"))
        self.actionPyQt.setText(_translate("MainWindow", "PyQt"))

