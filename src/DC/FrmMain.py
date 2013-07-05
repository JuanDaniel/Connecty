# -*- coding: utf-8 -*-
'''
Created on 04/07/2013

@author: jdsantana
'''
from PyQt4 import QtGui
from Visual.Main import Ui_MainWindow

class FrmMain(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(FrmMain, self).__init__(parent)
        self.setupUi(self)
