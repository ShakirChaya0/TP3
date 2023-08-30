import pickle 
import os.path
from datetime import date

class Usuarios:
    def __init__(self) -> None:
        self.CodUsuario = 0
        self.NombreUsuario = " ".ljust(100," ")
        self.ClaveUsuario = " ".ljust(8," ")
        self.TipoUsuario = " ".ljust(20," ")

class Locales:
    def __init__(self) -> None:
        self.CodLocal = 0
        self.NombreLocal = " ".ljust(50," ")
        self.UbiLocal = " ".ljust(50," ")
        self.RubroLocal = " ".ljust(50," ")
        self.CodUsuario = 0
        self.Estado = ""

class Promociones:
    def __init__(self) -> None:
        self.CodPromo = 0
        self.TextoPromo = " ".ljust(200," ")
        self.FechaDesdePromo = ""
        self.FechaHastaPromo = ""
        self.DiaSemana = [0] * 6 
        self.Estado = " ".ljust(10," ")
        self.CodLocal = 0

class Uso_Promocion:
    def __init__(self) -> None:
        self.CodCliente = 0
        self.CodPromo = 0
        self.FechaUsoPromo = ""

class Novedades:
    def __init__(self) -> None:
        self.CodNovedad = 0
        self.TextoNovedad = " ".ljust(200," ")
        self.FechaDesdeNovedad = ""
        self.FechaHastaNovedad = ""
        self.TipoUsuario = " ".ljust(20," ")
        self.Estado = ""


AFU = "C:\\TP3\\Archivos\\Usuarios.dat"
AFL = "C:\\TP3\\Archivos\\Locales.dat"
AFP = "C:\\TP3\\Archivos\\Promociones.dat"
AFUP = "C:\\TP3\\Archivos\\Uso_Promociones.dat"
AFN = "C:\\TP3\\Archivos\\Novedades.dat"

ALU = open(AFU,"r+b")
ALL = open(AFL, "r+b")
ALP = open(AFP, "r+b")
ALUP = open(AFUP, "r+b")
ALN = open(AFN, "r+b")

R_Usu = Usuarios()
R_Loc = Locales()
R_Pro = Promociones()
R_Uso_Pro = Uso_Promocion()
R_Nov = Novedades()

#jkfhdsfgffgfd hollaaa
if os.path.getsize(AFU) == 0: 
    R_Usu.CodUsuario = 1
    R_Usu.NombreUsuario = "admin".ljust(100," ")
    R_Usu.ClaveUsuario = "12345".ljust(8," ")
    R_Usu.TipoUsuario = "administrador".ljust(20," ")
    ALU.seek(0, 2)
    pickle.dump(R_Usu, ALU)
    ALU.flush()



