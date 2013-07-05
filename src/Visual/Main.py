# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Visual/UI/Main.ui'
#
# Created: Thu Jul  4 22:57:08 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(282, 385)
        MainWindow.setMinimumSize(QtCore.QSize(282, 385))
        MainWindow.setMaximumSize(QtCore.QSize(282, 385))
        MainWindow.setToolTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ssid = QtGui.QComboBox(self.centralwidget)
        self.ssid.setGeometry(QtCore.QRect(10, 90, 161, 24))
        self.ssid.setObjectName(_fromUtf8("ssid"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 150, 161, 28))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 200, 261, 161))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.start_service = QtGui.QPushButton(self.centralwidget)
        self.start_service.setGeometry(QtCore.QRect(190, 150, 85, 27))
        self.start_service.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/dialog-apply.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.start_service.setIcon(icon)
        self.start_service.setObjectName(_fromUtf8("start_service"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 0, 91, 81))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/network-wireless_1.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 282, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMen_u = QtGui.QMenu(self.menubar)
        self.menuMen_u.setObjectName(_fromUtf8("menuMen_u"))
        self.menuAyuda = QtGui.QMenu(self.menubar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
        MainWindow.setMenuBar(self.menubar)
        self.actionConfigurar = QtGui.QAction(MainWindow)
        self.actionConfigurar.setObjectName(_fromUtf8("actionConfigurar"))
        self.actionPerfiles = QtGui.QAction(MainWindow)
        self.actionPerfiles.setObjectName(_fromUtf8("actionPerfiles"))
        self.actionAcerca_de = QtGui.QAction(MainWindow)
        self.actionAcerca_de.setObjectName(_fromUtf8("actionAcerca_de"))
        self.menuMen_u.addAction(self.actionConfigurar)
        self.menuMen_u.addAction(self.actionPerfiles)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuMen_u.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Connecty", None))
        self.ssid.setToolTip(_translate("MainWindow", "Seleccione el perfil de conexión a iniciar", None))
        self.label.setText(_translate("MainWindow", "SSID", None))
        self.label_2.setText(_translate("MainWindow", "Clave", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Conectados", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Usuarios conectados actualmente", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Historial", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Historial de usuarios conectados", None))
        self.start_service.setToolTip(_translate("MainWindow", "Iniciar el servicio de conexión", None))
        self.start_service.setText(_translate("MainWindow", "Iniciar", None))
        self.menuMen_u.setTitle(_translate("MainWindow", "Menú", None))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda", None))
        self.actionConfigurar.setText(_translate("MainWindow", "Configurar", None))
        self.actionPerfiles.setText(_translate("MainWindow", "Perfiles", None))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de...", None))

import resources_rc
