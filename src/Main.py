# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 01/07/2013

@author: jdsantana
'''
from PyQt4.QtGui import QApplication
from Entorno.ImpMain import ImpMain

if __name__ == '__main__':
    app = QApplication([])
    frm = ImpMain(None)
    frm.Execute()
    app.exec_()