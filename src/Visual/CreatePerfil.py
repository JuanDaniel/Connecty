# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Visual/UI/CreatePerfil.ui'
#
# Created: Fri Jul  5 00:42:46 2013
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

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName(_fromUtf8("Wizard"))
        Wizard.resize(400, 222)
        Wizard.setMinimumSize(QtCore.QSize(400, 222))
        Wizard.setMaximumSize(QtCore.QSize(400, 222))
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.label = QtGui.QLabel(self.wizardPage1)
        self.label.setGeometry(QtCore.QRect(100, 10, 215, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.wizardPage1)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 131, 111))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/network-wireless_1.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.label_3 = QtGui.QLabel(self.wizardPage2)
        self.label_3.setGeometry(QtCore.QRect(100, 10, 206, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.wizardPage2)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 115, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.wizardPage2)
        self.label_5.setGeometry(QtCore.QRect(220, 80, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.interface_ap = QtGui.QComboBox(self.wizardPage2)
        self.interface_ap.setGeometry(QtCore.QRect(10, 100, 151, 24))
        self.interface_ap.setObjectName(_fromUtf8("interface_ap"))
        self.interface_share = QtGui.QComboBox(self.wizardPage2)
        self.interface_share.setGeometry(QtCore.QRect(220, 100, 151, 24))
        self.interface_share.setObjectName(_fromUtf8("interface_share"))
        Wizard.addPage(self.wizardPage2)
        self.wizardPage = QtGui.QWizardPage()
        self.wizardPage.setObjectName(_fromUtf8("wizardPage"))
        self.label_6 = QtGui.QLabel(self.wizardPage)
        self.label_6.setGeometry(QtCore.QRect(60, 10, 257, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.wizardPage)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.wizardPage)
        self.label_8.setGeometry(QtCore.QRect(230, 50, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.wizardPage)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.wizardPage)
        self.label_10.setGeometry(QtCore.QRect(230, 110, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.address = QtGui.QLineEdit(self.wizardPage)
        self.address.setGeometry(QtCore.QRect(10, 70, 141, 28))
        self.address.setObjectName(_fromUtf8("address"))
        self.network = QtGui.QLineEdit(self.wizardPage)
        self.network.setGeometry(QtCore.QRect(230, 70, 141, 28))
        self.network.setObjectName(_fromUtf8("network"))
        self.netmask = QtGui.QLineEdit(self.wizardPage)
        self.netmask.setGeometry(QtCore.QRect(10, 130, 141, 28))
        self.netmask.setObjectName(_fromUtf8("netmask"))
        self.gateway = QtGui.QLineEdit(self.wizardPage)
        self.gateway.setGeometry(QtCore.QRect(230, 130, 141, 28))
        self.gateway.setObjectName(_fromUtf8("gateway"))
        Wizard.addPage(self.wizardPage)
        self.wizardPage_2 = QtGui.QWizardPage()
        self.wizardPage_2.setObjectName(_fromUtf8("wizardPage_2"))
        self.label_11 = QtGui.QLabel(self.wizardPage_2)
        self.label_11.setGeometry(QtCore.QRect(120, 10, 148, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.wizardPage_2)
        self.label_12.setGeometry(QtCore.QRect(10, 70, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.wizardPage_2)
        self.label_13.setGeometry(QtCore.QRect(220, 70, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.ssid = QtGui.QLineEdit(self.wizardPage_2)
        self.ssid.setGeometry(QtCore.QRect(10, 90, 151, 28))
        self.ssid.setObjectName(_fromUtf8("ssid"))
        self.password = QtGui.QLineEdit(self.wizardPage_2)
        self.password.setGeometry(QtCore.QRect(220, 90, 151, 28))
        self.password.setObjectName(_fromUtf8("password"))
        Wizard.addPage(self.wizardPage_2)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(_translate("Wizard", "Crear un nuevo perfil", None))
        self.label.setText(_translate("Wizard", "Haz tu PC un Access Point", None))
        self.label_3.setText(_translate("Wizard", "Seleccione las interfaces", None))
        self.label_4.setText(_translate("Wizard", "Inalámbrica", None))
        self.label_5.setToolTip(_translate("Wizard", "Seleccione la interfaz a compartir la conexión", None))
        self.label_5.setText(_translate("Wizard", "Internet", None))
        self.interface_ap.setToolTip(_translate("Wizard", "Seleccione la interfaz a usar como AP", None))
        self.label_6.setText(_translate("Wizard", "Parámetros de la nueva subred", None))
        self.label_7.setText(_translate("Wizard", "Address", None))
        self.label_8.setToolTip(_translate("Wizard", "Dirección de subred", None))
        self.label_8.setText(_translate("Wizard", "Network", None))
        self.label_9.setToolTip(_translate("Wizard", "Máscara de la subred", None))
        self.label_9.setText(_translate("Wizard", "Netmask", None))
        self.label_10.setToolTip(_translate("Wizard", "Dirección de gateway", None))
        self.label_10.setText(_translate("Wizard", "Gateway", None))
        self.address.setToolTip(_translate("Wizard", "Dirección IP para el AP", None))
        self.label_11.setText(_translate("Wizard", "Ya casi está listo!!", None))
        self.label_12.setText(_translate("Wizard", "SSID", None))
        self.label_13.setText(_translate("Wizard", "Clave", None))
        self.ssid.setToolTip(_translate("Wizard", "Determine el nombre para la nueva conexión", None))
        self.password.setToolTip(_translate("Wizard", "Proporcione la clave de acceso", None))

import resources_rc
