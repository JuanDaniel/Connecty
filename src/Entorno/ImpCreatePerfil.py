'''
Created on 04/07/2013

@author: jdsantana
'''
from DC.FrmCreatePerfil import FrmCreatePerfil

class ImpCreatePerfil:

    def __init__(self, parent):
        self.__frm = FrmCreatePerfil(parent)

    def __loadInterfaces(self):
        pass

    def Execute(self):
        self.__frm.show()