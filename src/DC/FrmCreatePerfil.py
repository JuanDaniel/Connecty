# -*- coding: utf-8 -*-
'''
Created on 04/07/2013

@author: jdsantana
'''
from PyQt4 import QtGui
from Visual.CreatePerfil import Ui_Wizard
from PyQt4.QtGui import QMessageBox

class FrmCreatePerfil(QtGui.QWizard, Ui_Wizard):

    def __init__(self, parent = None):
        super(FrmCreatePerfil, self).__init__(parent)
        self.setupUi(self)

    def validateCurrentPage(self):
        if(self.currentId() == 1):
            return self.__checkInterfaces()

        return True

    def __checkInterfaces(self):
        if(self.interface_ap.currentText().isEmpty() or
           self.interface_share.currentText().isEmpty()):
            QMessageBox.critical(self, u"Interfaces vacías", "Debe especificar ambas interfaces")
            return False
        if(self.interface_ap.currentText() == self.interface_share.currentText()):
            QMessageBox.critical(self, u"Interfaces inválidas", u"Debe especificar interfaces distintas.\n Recuerde, una servirá para difundir la señal inalámbrica y la otra para compartir la conexión")
            return False

        return True