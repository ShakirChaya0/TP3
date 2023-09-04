import getpass
import pickle
import os.path
from datetime import date


class Usuarios:
    def __init__(self) -> None:
        self.CodUsuario = 0
        self.NombreUsuario = " ".ljust(100, " ")
        self.ClaveUsuario = " ".ljust(8, " ")
        self.TipoUsuario = " ".ljust(20, " ")


class Locales:
    def __init__(self) -> None:
        self.CodLocal = 0
        self.NombreLocal = " ".ljust(50, " ")
        self.UbiLocal = " ".ljust(50, " ")
        self.RubroLocal = " ".ljust(50, " ")
        self.CodUsuario = 0
        self.Estado = ""


class Promociones:
    def __init__(self) -> None:
        self.CodPromo = 0
        self.TextoPromo = " ".ljust(200, " ")
        self.FechaDesdePromo = ""
        self.FechaHastaPromo = ""
        self.DiaSemana = [0] * 6
        self.Estado = " ".ljust(10, " ")
        self.CodLocal = 0


class Uso_Promocion:
    def __init__(self) -> None:
        self.CodCliente = 0
        self.CodPromo = 0
        self.FechaUsoPromo = ""


class Novedades:
    def __init__(self) -> None:
        self.CodNovedad = 0
        self.TextoNovedad = " ".ljust(200, " ")
        self.FechaDesdeNovedad = ""
        self.FechaHastaNovedad = ""
        self.TipoUsuario = " ".ljust(20, " ")
        self.Estado = ""


def separador():
    print(70 * "-")


def pedirusuario():
    global cod
    global eleccion
    global bandera
    contador = 0

    # Ingreso de datos:
    user = input("Escriba su usuario: ").ljust(100, " ")
    contraseña = getpass.getpass("Escriba su contraseña: ").ljust(8, " ")
    ALU.seek(0, 0)
    cont = pickle.load(ALU)
    pre = Bs_Usu(cont.NombreUsuario, user)
    if pre != -1:
        if cont.ClaveUsuario == contraseña:
            cod = cont.TipoUsuario.strip()
        else:
            cod = ""
    else:
        cod = ""

    # Restricción de intentos del inicio de sesión
    while cod == "" and contador < 3:
        contador = contador + 1
        os.system("cls")
        if contador <= 2:
            user = input("Escriba su usuario: ").ljust(100, " ")
            contraseña = getpass.getpass("Escriba su contraseña: ").ljust(8, " ")
            ALU.seek(0, 0)
            cont = pickle.load(ALU)
            pre = Bs_Usu(cont.NombreUsuario, user)
            if pre != -1:
                ent = Bs_Usu(cont.ClaveUsuario, contraseña)
                if ent != -1:
                    cod = cont.TipoUsuario
                else:
                    cod = ""
            else:
                cod = ""
        else:
            print("Su numero de intentos ha finalizado")
            bandera = -1
            eleccion = 0
    if cod != "":
        os.system("cls")
        print("- Hola, has ingresado correctamente")


def mostrar_menu():
    if cod == 1:
        if eleccion != 1 and eleccion != 4 and eleccion != 0:
            print(
                """\033[1;36m---------------Menu principal Administrador---------------\033[0;m
      0. Salir
      1. Gestion de locales
      2. Crear cuentas de dueños de locales
      3. Aprobar / Denegar solicitud de descuento
      4. Gestión de Novedades
      5. Reporte de utilización de descuentos"""
            )

        elif eleccion == 1:
            print(
                """\033[;32m---------------Gestión de locales---------------\033[0;m
        a) Crear locales
        b) Modificar local
        c) Eliminar local
        d) Mapa de locales
        e) Volver"""
            )

        elif eleccion == 4:
            print(
                """\033[;32m---------------Gestión de Novedades---------------\033[0;m
        a) Crear novedades
        b) Modificar novedad
        c) Eliminar novedad
        d) Ver reporte de novedades
        e) Volver"""
            )

    elif cod == 4 or cod == 6:
        print(
            """\033[1;36m---------------Menu principal Dueños Locales---------------\033[0;m
      1. Gestión de Descuentos
      a) Crear descuento para mi local
      b) Modificar descuento de mi local
      c) Eliminar descuento de mi local
      d) Volver
      2. Aceptar / Rechazar pedido de descuento
      3. Reporte de uso de descuentos
      0. Salir"""
        )

    else:
        print(
            """\033[1;36m---------------Menu principal Cliente---------------\033[0;m
      1. Registrarme
      2. Buscar descuentos en locales
      3. Solicitar descuento
      4. Ver novedades
      0. Salir"""
        )


def Menu_principal():
    print(
        """
      1. Ingresar con usuario registrado
      2. Registrarse como cliente
      3. Salir
      """
    )


# Busqueda secuencial para registro Usuarios
def Bs_Usu(X, valor):
    T = os.path.getsize(AFU)
    pos = 1
    ALU.seek(0, 0)
    cont = pickle.load(ALU)
    while ALU.tell() < T and X != valor:
        pos = ALU.tell()
        cont = pickle.load(ALU)
    if valor == X:
        cont = pos
    else:
        cont = -1
    return cont


# Validación de numeros
def Validar(nro, desde, hasta):
    try:
        nro = int(nro)
        if nro >= desde and nro <= hasta:
            return True
        else:
            return False
    except:
        return False


def Registrarse():
    global i_global
    R_Usu.NombreUsuario = input("Ingrese el mail del usuario: ").ljust(100, " ")
    # Hacer busqueda secuencial para verificar que no se repite el usuario...
    while len(R_Usu.NombreUsuario) >= 100:
        print("Usted ingreso un mail muy largo, intente otra vez")
        R_Usu.NombreUsuario = input("Ingrese la clave del usuario: ").ljust(100, " ")

    R_Usu.ClaveUsuario = input("Ingrese la clave del usuario: ").ljust(8, " ")
    while len(R_Usu.ClaveUsuario) >= 8:
        print("Usted ingreso una clave muy larga, intente otra vez")
        R_Usu.ClaveUsuario = input("Ingrese la clave del usuario: ").ljust(8, " ")

    R_Usu.TipoUsuario = "cliente"
    R_Usu.CodUsuario = i_global
    i_global = i_global + 1
    pickle.dump(R_Usu, ALU)
    ALU.flush()


def Admin():
    print("A")


def DueñoDelocales():
    print("D")


def Clientes():
    print("C")


# Declaración de variables...
bandera = 0
i_global = 1

# Declaración de variables que contienen la ubicación física de los archivos
AFU = "C:\\TP3\\Archivos\\Usuarios.dat"
AFL = "C:\\TP3\\Archivos\\Locales.dat"
AFP = "C:\\TP3\\Archivos\\Promociones.dat"
AFUP = "C:\\TP3\\Archivos\\Uso_Promociones.dat"
AFN = "C:\\TP3\\Archivos\\Novedades.dat"

# Declaración de las variables que contienen a los archivos abiertos
ALU = open(AFU, "r+b")
ALL = open(AFL, "r+b")
ALP = open(AFP, "r+b")
ALUP = open(AFUP, "r+b")
ALN = open(AFN, "r+b")

# Declaración de las variables que contienen a los registros
R_Usu = Usuarios()
R_Loc = Locales()
R_Pro = Promociones()
R_Uso_Pro = Uso_Promocion()
R_Nov = Novedades()

if os.path.getsize(AFU) == 0:
    R_Usu.CodUsuario = i_global
    i_global = i_global + 1
    R_Usu.NombreUsuario = "admin".ljust(100, " ")
    R_Usu.ClaveUsuario = "12345".ljust(8, " ")
    R_Usu.TipoUsuario = "administrador".ljust(20, " ")
    ALU.seek(0, 2)
    pickle.dump(R_Usu, ALU)
    ALU.flush()


####### PROGRAMA PRINCIPAL ########

Menu_principal()
elec = input("Seleccione la opción que desee: ")
while elec != 3 and bandera == 0:
    try:
        elec = int(elec)
        adm = "administrador"
        if elec == 1:
            pedirusuario()
            match cod.strip():
                case "administrador":
                    Admin()
                case "dueños de local":
                    DueñoDelocales()
                case "cliente":
                    Clientes()
        elif elec == 1 or elec == 2:
            Registrarse()
        elif elec == 3:
            print("Hasta luego...")
            bandera = -1
        if bandera == 0:
            Menu_principal()
            elec = input("Seleccione la opción que desee: ")
    except:
        elec = input("Valor equivocado, intente ingresar una de las opciones dadas: ")
