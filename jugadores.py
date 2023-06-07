from datetime import datetime

class Jugadores:

    def __init__(self, Id):
        # Id de jugador
        self.id = Id
        # Contador de tiempo
        self.cnt = 60
        # Bandera de error
        self.err = 0
        self.inT = 0
        self.pvT = 0
        self.rst = 0
        self.pts = 0

    def setId(self, Num):
        self.num = Num

    def setCnt(self, Cnt):
        self.cnt = Cnt

    def setErr(self, Err):
        self.err = Err

    def setInT(self):
        self.inT = datetime.now().second

    def checkTim(self):

        Now = datetime.now().second
        Diff = int(Now) - int(self.inT)

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
