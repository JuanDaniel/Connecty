'''
Created on 04/07/2013

@author: jdsantana
'''
from DC.FrmMain import FrmMain
import os
from Entorno.ImpCreatePerfil import ImpCreatePerfil

class ImpMain:

    def __init__(self, parent):
        self.__frm = FrmMain(parent)
        self.__perfils = []

    def __loadPerfils(self):
        if(not os.path.exists(os.path.expanduser('~/.Connecty/perfils'))):
            #os.makedirs(os.path.expanduser('~/.Connecty/perfils'))
            print 'lanzo la interfaz de configuracion de los perfiles'
            self.__createPerfil()

    def __createPerfil(self):
        self.__instance = ImpCreatePerfil(self.__frm)
        self.__instance.Execute()

    def Execute(self):
        self.__loadPerfils()
        self.__frm.show()


