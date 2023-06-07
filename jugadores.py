# Librerías
from datetime import datetime

# Clase de jugadores
class Jugadores:
    # Definición
    def __init__(self, Id):
        # Id de jugador
        self.id = Id
        # Puntos
        self.pts = 0
        # Contador de tiempo
        self.cnt = 60
        # Tiempo inicial
        self.inT = 0
        # Tiempo previo
        self.pvT = 0
        # Bandera de error
        self.err = 0
        # Bandera de reset
        self.rst = 0
        # Colores
        self.colores = []
    
    # Set Id
    def setId(self, Num):
        self.num = Num

    # Set count
    def setCnt(self, Cnt):
        self.cnt = Cnt

    # Set error
    def setErr(self, Err):
        self.err = Err

    # Set initial time
    def setInT(self):
        self.inT = datetime.now().second

    def checkTim(self):

        Now = datetime.now().second
        Diff = int(Now) - int(self.inT)

        if Now == 0:
            self.inT = datetime.now().second
            self.pvT = datetime.now().second

        if self.rst == 0:
            if self.pvT < Diff:
                self.cnt -= 1
                self.pvT = Diff

            if self.err == 1:
                self.cnt -= 10
                self.err = 0

            if self.cnt <= 0:
                self.cnt = 60
                self.rst = 1
            
    #def ensenarColores(self):
        
        
