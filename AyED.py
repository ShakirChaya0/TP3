import getpass
import pickle
import os.path
import os
import sys
import datetime


class Usuarios:
    def __init__(self) -> None:
        self.CodUsuario = 0
        self.NombreUsuario = " ".ljust(100, " ")
        self.ClaveUsuario = " ".ljust(8, " ")
        self.TipoUsuario = " ".ljust(20, " ")


class Locales:
    def __init__(self) -> None:
        self.CodLocal = 0
        self.NombreLocal = " ".ljust(30, " ")
        self.UbiLocal = " ".ljust(30, " ")
        self.RubroLocal = " ".ljust(12, " ")
        self.CodUsuario = 0
        self.Estado = ""


class Promociones:
    def __init__(self) -> None:
        self.CodPromo = 0
        self.TextoPromo = "".ljust(200, " ")
        self.FechaDesdePromo = ""
        self.FechaHastaPromo = ""
        self.DiaSemana = [0] * 7
        self.Estado = "".ljust(10, " ")
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

class R_Rub:
    def __init__(self) -> None:
        self.Nom = " ".ljust(12," ")
        self.Ca = 0

Rubros = [R_Rub] * 3
#Instanciando las clases para asignar los atributos respectivos
cl1 = R_Rub()
cl1.Nom = "perfumeria".ljust(12," ")
cl1.Ca = 0
Rubros[0] = cl1
cl2 = R_Rub()
cl2.Nom = "indumentaria".ljust(12," ")
cl2.Ca = 0
Rubros[1] = cl2
cl3 = R_Rub()
cl3.Nom = "comida".ljust(12," ")
cl3.Ca = 0
Rubros[2] = cl3


""""""
""""""
""""""
""""""
""""""
""""""
""""""

# SECCIÓN DE DETALLES ESTÉTICOS # (Inicio)


def separador():
    print(70 * "-")


def Exhibicion():
    if os.path.getsize(AFL) != 0:
        or_archivo()
        ALL.seek(0, 0)
        Aux_I = pickle.load(ALL)
        T_RL = ALL.tell()
        T_AL = os.path.getsize(AFL)
        C_RL = round(T_AL / T_RL) 
        i = 0
        borde = "║"
        label = "║Codigo local"
        label += borde
        label += "Codigo Usuario"
        label += borde
        label += " " * 12
        label += "Nombre"
        label += " " * 12
        label += borde
        label += " " * 10
        label += "Ubicacion"
        label += " " * 11
        label += borde
        label += " " * 3
        label += "Rubro"
        label += " " * 4
        label += borde
        label += "Estado║"
        sys.stdout.write("╔")
        sys.stdout.write(12 * "═")
        sys.stdout.write("╦")
        sys.stdout.write(14 * "═")
        sys.stdout.write("╦")
        sys.stdout.write(30 * "═")
        sys.stdout.write("╦")
        sys.stdout.write(30 * "═")
        sys.stdout.write("╦")
        sys.stdout.write(12 * "═")
        sys.stdout.write("╦")
        sys.stdout.write(6 * "═")
        sys.stdout.write("╗\n")
        print(label)
        while ALL.tell() <= T_AL:
            sys.stdout.write("╠")
            sys.stdout.write(12 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(14 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(30 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(30 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(12 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(6 * "═")
            sys.stdout.write("╣\n")
            ALL.seek(i * T_RL, 0)
            Auxiliar = pickle.load(ALL)
            item = ""
            item += "║"
            item += str(Auxiliar.CodLocal).center(12)
            item += borde
            item += str(Auxiliar.CodUsuario).center(14)
            item += borde
            item += Auxiliar.NombreLocal.strip().center(30)
            item += borde
            item += Auxiliar.UbiLocal.strip().center(30)
            item += borde
            item += Auxiliar.RubroLocal.strip().center(12)
            item += borde
            item += Auxiliar.Estado.center(6)
            item += "║"
            i += 1
            ALL.seek((i * T_RL) +20 , 0)
            print(item)
        sys.stdout.write("╚")
        sys.stdout.write(12 * "═")
        sys.stdout.write("╩")
        sys.stdout.write(14 * "═")
        sys.stdout.write("╩")
        sys.stdout.write(30 * "═")
        sys.stdout.write("╩")
        sys.stdout.write(30 * "═")
        sys.stdout.write("╩")
        sys.stdout.write(12 * "═")
        sys.stdout.write("╩")
        sys.stdout.write(6 * "═")
        sys.stdout.write("╝\n")
    else:
        print("Aun no hay ningún local cargado")

def Exhibicion_Prom():
    if os.path.getsize(AFP) != 0:
        ALP.seek(0, 0)
        Aux_I = pickle.load(ALP)
        T_RP = ALP.tell()
        T_AP = os.path.getsize(AFP)
        C_RP = round(T_AP / T_RP) 
        i = 0
        borde = "║"
        label = "║Codigo Promo"
        label += borde
        label += " " * 15
        label += "Texto Promo"
        label += " " * 15
        label += borde
        label += " " * 5
        label += "Fecha Desde"
        label += " " * 5
        label += borde
        label += " " * 5
        label += "Fecha Hasta"
        label += " " * 5
        label += borde
        label += "Dia Semana"
        label += borde
        label += " " * 4
        label += "Estado"
        label += " " * 4
        label += borde
        label += " Cod Local║"
        label += " " 
        sys.stdout.write("╔")
        sys.stdout.write(12 * "═")
        sys.stdout.write("╦")
        sys.stdout.write(14 * "═")
        sys.stdout.write("╦")
        sys.stdout.write(30 * "═")
        sys.stdout.write("╦")
        sys.stdout.write(30 * "═")
        sys.stdout.write("╦")
        sys.stdout.write(22 * "═")
        sys.stdout.write("╦")
        sys.stdout.write(14 * "═")
        sys.stdout.write("╦")
        sys.stdout.write(10 * "═")
        sys.stdout.write("╗\n")
        print(label)
        while ALP.tell() <= T_AP:
            sys.stdout.write("╠")
            sys.stdout.write(12 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(14 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(30 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(30 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(22 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(14 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(10 * "═")
            sys.stdout.write("╣\n")
            ALP.seek(i * T_RP, 0)
            R_Pro = pickle.load(ALP)
            item = ""
            item += "║"
            item += str(R_Pro.CodPromo).center(12)
            item += borde
            item += R_Pro.TextoPromo.strip().center(14)
            item += borde
            item += str(R_Pro.FechaDesdePromo).center(30)
            item += borde
            item += str(R_Pro.FechaHastaPromo).center(30)
            item += borde
            item += str(R_Pro.DiaSemana).center(12)
            item += " "
            item += borde
            item += R_Pro.Estado.center(14)
            item += borde
            item += str(R_Pro.CodLocal).center(8)
            item += "║"
            i += 1
            ALP.seek((i * T_RP) + 20 , 0)
            print(item)
        sys.stdout.write("╚")
        sys.stdout.write(12 * "═")
        sys.stdout.write("╩")
        sys.stdout.write(14 * "═")
        sys.stdout.write("╩")
        sys.stdout.write(30 * "═")
        sys.stdout.write("╩")
        sys.stdout.write(30 * "═")
        sys.stdout.write("╩")
        sys.stdout.write(22 * "═")
        sys.stdout.write("╩")
        sys.stdout.write(14 * "═")
        sys.stdout.write("╩")
        sys.stdout.write(10 * "═")
        sys.stdout.write("╝\n")
    else:
        print("Aun no hay ninguna promoción cargada")

def Exhibicion_Clientes_Desc():
    borde = "║"
    label = "║Codigo Promo"
    label += borde
    label += " " * 15
    label += "Texto Promo"
    label += " " * 15
    label += borde
    label += " " * 5
    label += "Fecha Desde"
    label += " " * 5
    label += borde
    label += " " * 5
    label += "Fecha Hasta"
    label += " " * 5
    label += borde
    sys.stdout.write("╔")
    sys.stdout.write(12 * "═")
    sys.stdout.write("╦")
    sys.stdout.write(41 * "═")
    sys.stdout.write("╦")
    sys.stdout.write(21 * "═")
    sys.stdout.write("╦")
    sys.stdout.write(21 * "═")
    sys.stdout.write("╗\n")
    print(label)
    ALP.seek(0,0)
    while ALP.tell() < os.path.getsize(AFP):
        R_Pro = pickle.load(ALP)
        if R_Pro.Estado.strip() == "aprobada" and R_Pro.FechaDesdePromo <= datetime.date.today() and R_Pro.FechaHastaPromo >= datetime.date.today():
          if R_Pro.DiaSemana[datetime.date.today().weekday()] == 1:
                sys.stdout.write("╠")
                sys.stdout.write(12 * "═")
                sys.stdout.write("╬")
                sys.stdout.write(41 * "═")
                sys.stdout.write("╬")
                sys.stdout.write(21 * "═")
                sys.stdout.write("╬")
                sys.stdout.write(21 * "═")
                sys.stdout.write("╣\n")
                item = ""
                item += "║"
                item += str(R_Pro.CodPromo).center(12)
                item += borde
                item += R_Pro.TextoPromo.strip().center(41)
                item += borde
                item += str(R_Pro.FechaDesdePromo).center(21)
                item += borde
                item += str(R_Pro.FechaHastaPromo).center(21)
                item += "║"
                print(item)
    sys.stdout.write("╚")
    sys.stdout.write(12 * "═")
    sys.stdout.write("╩")
    sys.stdout.write(41 * "═")
    sys.stdout.write("╩")
    sys.stdout.write(21 * "═")
    sys.stdout.write("╩")
    sys.stdout.write(21 * "═")
    sys.stdout.write("╝\n")

def Exhibicion_Clientes(Cod_local, Fecha):
    borde = "║"
    label = "║Codigo Promo"
    label += borde
    label += " " * 15
    label += "Texto Promo"
    label += " " * 15
    label += borde
    label += " " * 5
    label += "Fecha Desde"
    label += " " * 5
    label += borde
    label += " " * 5
    label += "Fecha Hasta"
    label += " " * 5
    label += borde
    sys.stdout.write("╔")
    sys.stdout.write(12 * "═")
    sys.stdout.write("╦")
    sys.stdout.write(41 * "═")
    sys.stdout.write("╦")
    sys.stdout.write(21 * "═")
    sys.stdout.write("╦")
    sys.stdout.write(21 * "═")
    sys.stdout.write("╗\n")
    print(label)
    ALP.seek(0,0)
    while ALP.tell() < os.path.getsize(AFP):
        R_Pro = pickle.load(ALP)
        if R_Pro.CodLocal == Cod_local and R_Pro.Estado.strip() == "aprobada" and R_Pro.FechaDesdePromo <= Fecha and R_Pro.FechaHastaPromo >= Fecha:
          if R_Pro.DiaSemana[Fecha.weekday()] == 1:
                sys.stdout.write("╠")
                sys.stdout.write(12 * "═")
                sys.stdout.write("╬")
                sys.stdout.write(41 * "═")
                sys.stdout.write("╬")
                sys.stdout.write(21 * "═")
                sys.stdout.write("╬")
                sys.stdout.write(21 * "═")
                sys.stdout.write("╣\n")
                item = ""
                item += "║"
                item += str(R_Pro.CodPromo).center(12)
                item += borde
                item += R_Pro.TextoPromo.strip().center(41)
                item += borde
                item += str(R_Pro.FechaDesdePromo).center(21)
                item += borde
                item += str(R_Pro.FechaHastaPromo).center(21)
                item += "║"
                print(item)
    sys.stdout.write("╚")
    sys.stdout.write(12 * "═")
    sys.stdout.write("╩")
    sys.stdout.write(41 * "═")
    sys.stdout.write("╩")
    sys.stdout.write(21 * "═")
    sys.stdout.write("╩")
    sys.stdout.write(21 * "═")
    sys.stdout.write("╝\n")

def Exhibicion_Reportes(Fecha_d,Fecha_h, Cod):
    borde = "║"
    label = "║Codigo Promo"
    label += borde
    label += " " * 15
    label += "Texto Promo"
    label += " " * 15
    label += borde
    label += " " * 5
    label += "Fecha Desde"
    label += " " * 5
    label += borde
    label += " " * 5
    label += "Fecha Hasta"
    label += " " * 5
    label += borde
    label += "Cantidad de Usos"
    label += borde
    sys.stdout.write("╔")
    sys.stdout.write(12 * "═")
    sys.stdout.write("╦")
    sys.stdout.write(41 * "═")
    sys.stdout.write("╦")
    sys.stdout.write(21 * "═")
    sys.stdout.write("╦")
    sys.stdout.write(21 * "═")
    sys.stdout.write("╦")
    sys.stdout.write(16 * "═")
    sys.stdout.write("╗\n")
    print(label)
    ALP.seek(0,0)
    while ALP.tell() < os.path.getsize(AFP):
        R_Pro = pickle.load(ALP)
        if R_Pro.Estado.strip() == "aprobada" and Fecha_d <= R_Pro.FechaDesdePromo and Fecha_h >= R_Pro.FechaHastaPromo and Cod == R_Pro.CodLocal: 
            sys.stdout.write("╠")
            sys.stdout.write(12 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(41 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(21 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(21 * "═")
            sys.stdout.write("╬")
            sys.stdout.write(16 * "═")
            sys.stdout.write("╣\n")
            item = "║"
            item += str(R_Pro.CodPromo).center(12)
            item += borde
            item += R_Pro.TextoPromo.strip().center(41)
            item += borde
            item += str(R_Pro.FechaDesdePromo).center(21)
            item += borde
            item += str(R_Pro.FechaHastaPromo).center(21)
            item += borde
            item += str(Conteo_Usos(R_Pro.CodPromo)).center(16)
            item += "║"
            print(item)
    sys.stdout.write("╚")
    sys.stdout.write(12 * "═")
    sys.stdout.write("╩")
    sys.stdout.write(41 * "═")
    sys.stdout.write("╩")
    sys.stdout.write(21 * "═")
    sys.stdout.write("╩")
    sys.stdout.write(21 * "═")
    sys.stdout.write("╩")
    sys.stdout.write(16 * "═")
    sys.stdout.write("╝\n")

def Conteo_Usos(X):
    if os.path.getsize(AFUP) != 0:
        cont = 0
        ALUP.seek(0,0)
        while ALUP.tell() < os.path.getsize(AFUP):
            R_Uso_Pro = pickle.load(ALUP)
            if R_Uso_Pro.CodPromo == X:
                cont = cont + 1
        return cont
    else:
        return 0

# SECCIÓN DE DETALLES ESTÉTICOS # (Final)

""""""
""""""
""""""
""""""
""""""
""""""
""""""

# SECCIÓN DE BUSQUEDAS, ORDENAMIENTOS Y OTRAS FUNCIONES# (Inicio)


def Bs_Usu(valor):
    T = os.path.getsize(AFU)
    pos = 0
    ALU.seek(0, 0)
    cont = pickle.load(ALU)
    while ALU.tell() < T and cont.NombreUsuario != valor:
        pos = ALU.tell()
        cont = pickle.load(ALU)
    if cont.NombreUsuario == valor:
        return pos
    else:
        return -1

def Bs_Usu_Cod(valor):
    T = os.path.getsize(AFU)
    pos = 0
    ALU.seek(0, 0)
    cont = pickle.load(ALU)
    while ALU.tell() < T and cont.CodUsuario != valor:
        pos = ALU.tell()
        cont = pickle.load(ALU)
    if cont.CodUsuario == valor:
        return pos
    else:
        return -1

def Bs_Usu_Tipo(valor):
    T = os.path.getsize(AFU)
    pos = 0
    ALU.seek(0, 0)
    cont = pickle.load(ALU)
    while ALU.tell() < T and cont.TipoUsuario != valor:
        pos = ALU.tell()
        cont = pickle.load(ALU)
    if cont.TipoUsuario == valor:
        return pos
    else:
        return -1

def Bs_Loc(valor):
    T = os.path.getsize(AFL)
    pos = 0
    ALL.seek(0, 0)
    cont = pickle.load(ALL)
    while ALL.tell() < T and cont.CodLocal != valor:
        pos = ALL.tell()
        cont = pickle.load(ALL)
    if cont.CodLocal == valor:
        return pos
    else:
        return -1

def or_archivo():
    ALL.seek(0, 0)
    Aux_I = pickle.load(ALL)
    T_RL = ALL.tell()
    C_RL = int(os.path.getsize(AFL) / T_RL)
    for i in range(0, C_RL - 1):
        for j in range(i + 1, C_RL):
            ALL.seek(i * T_RL, 0)
            Aux_I = pickle.load(ALL)
            ALL.seek(j * T_RL, 0)
            Aux_J = pickle.load(ALL)
            if Aux_I.NombreLocal > Aux_J.NombreLocal:
                ALL.seek(i * T_RL, 0)
                pickle.dump(Aux_J, ALL)
                ALL.seek(j * T_RL, 0)
                pickle.dump(Aux_I, ALL)
                ALL.flush()

def Bd_archivo(X):
    ALL.seek(0, 0)
    R_L = pickle.load(ALL)
    T_RL = ALL.tell()
    C_RL = int(os.path.getsize(AFL) / T_RL)
    inf = 0
    sup = C_RL - 1
    medio = (inf + sup) // 2
    ALL.seek(medio * T_RL, 0)
    R_L = pickle.load(ALL)
    while inf < sup and R_L.NombreLocal.strip() != X:
        if X < R_L.NombreLocal.strip():
            sup = medio - 1
        else:
            inf = medio + 1
        medio = (inf + sup) // 2
        if medio >= 0:
            ALL.seek(medio * T_RL, 0)
            R_L = pickle.load(ALL)
    if R_L.NombreLocal.strip() == X:
        return medio * T_RL
    else:
        return -1

def Bs_Sec_R(arreglo, valor):
    p = 0
    while arreglo[p] != valor and p < i_global:
        p = p + 1
    if arreglo[p] == valor:
        return p
    else:
        return -1

def Bs_pro(valor):
    M = os.path.getsize(AFP)
    pos = 0
    ALP.seek(0, 0)
    R_Pro = pickle.load(ALP)
    while ALP.tell() < M and R_Pro.CodPromo != valor:
        pos = ALP.tell()
        R_Pro = pickle.load(ALP)
    if R_Pro.CodPromo == valor:
        return pos
    else:
        return -1

def Bs_pro_Estado(valor):
    M = os.path.getsize(AFP)
    pos = 0
    ALP.seek(0, 0)
    R_Pro = pickle.load(ALP)
    while ALP.tell() < M and R_Pro.Estado != valor:
        pos = ALP.tell()
        R_Pro = pickle.load(ALP)
    if R_Pro.Estado == valor:
        return pos
    else:
        return -1

def Validacion(desde, hasta, mensaje):
    while True:
        try:
            numero = int(
                input(f"{mensaje}, número entre {desde} y {hasta}: ")
            )
            if desde <= numero <= hasta:
                return numero
            else:
                print(
                    f"El número debe estar entre {desde} y {hasta}. Inténtalo de nuevo."
                )
        except ValueError:
            print("¡Eso no es un número válido! Inténtalo de nuevo.")

def Validacion_Clientes(desde, hasta, mensaje):
    while True:
        try:
            numero = int(
                input(f"{mensaje}, hay {hasta} locales: ")
            )
            if desde <= numero <= hasta:
                return numero
            else:
                print(
                    f"El número debe estar entre {desde} y {hasta}. Inténtalo de nuevo."
                )
        except ValueError:
            print("¡Eso no es un número válido! Inténtalo de nuevo.")

def Validacion_Promos(desde, hasta, mensaje):
    while True:
        try:
            numero = int(
                input(f"{mensaje}")
            )
            if desde <= numero <= hasta:
                return numero
            else:
                print(
                    f"No es un numero valido, inténtalo de nuevo..."
                )
        except ValueError:
            print("¡Eso no es un número válido! Inténtalo de nuevo.")

def Validacion_fecha():
    while True: #NO SE PUEDE PONER TRUE, HAY QUE USAR BANDERAS
        try:
            fecha_str = input("Por favor ingresa una fecha en el formato YYYY-MM-DD: ")
            fecha_ingresada = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
            
            fecha_actual = datetime.datetime.now().date()
            
            if fecha_ingresada >= fecha_actual:
                return fecha_ingresada
            else:
                print("La fecha ingresada debe ser mayor o igual a la fecha actual. Inténtalo de nuevo.")
        except ValueError:
            print("¡Eso no es una fecha válida en el formato correcto (YYYY-MM-DD)! Inténtalo de nuevo.")

def Validacion_RangoI_Reporte():
    while True: 
        try:
            fecha_str = input("Por favor ingresa la fecha de inicio en el formato YYYY-MM-DD: ")
            fecha_ingresada = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
            return fecha_ingresada  
        except ValueError:
            print("¡Eso no es una fecha válida en el formato correcto (YYYY-MM-DD)! Inténtalo de nuevo.")

def Validacion_RangoF_Reporte(X):
    while True: 
        try:
            fecha_str = input("Por favor ingresa la fecha de fin en el formato YYYY-MM-DD: ")
            fecha_ingresada = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
            
            if fecha_ingresada >= X:
                return fecha_ingresada
            else:
                print("La fecha ingresada debe ser mayor o igual a la fecha de inicio. Inténtalo de nuevo.")
        except ValueError:
            print("¡Eso no es una fecha válida en el formato correcto (YYYY-MM-DD)! Inténtalo de nuevo.")


def Validacion_fecha_Desde():
    while True:
        try:
            fecha_str = input("Por favor ingresa la fecha de inicio de la promoción, en el formato YYYY-MM-DD: ")
            fecha_ingresada = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
            
            fecha_actual = datetime.datetime.now().date()
            
            if fecha_ingresada >= fecha_actual:
                return fecha_ingresada
            else:
                print("La fecha ingresada debe ser mayor o igual a la fecha actual. Inténtalo de nuevo.")
        except ValueError:
            print("¡Eso no es una fecha válida en el formato correcto (YYYY-MM-DD)! Inténtalo de nuevo.")


# SECCIÓN DE BUSQUEDAS, ORDENAMIENTOS Y OTRAS FUNCIONES# (Final)

""""""
""""""
""""""
""""""
""""""
""""""
""""""

# SECCIÓN DE MENUS # (Inicio)


def mostrar_menu():
    if cod == "administrador":
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
            print("Diagramado en chapín, para volver al menu oprima la letra e")

    elif cod == "dueño de local":
        print(
            """\033[1;36m---------------Menu principal Dueños Locales---------------\033[0;m
    1. Crear descuento
    2. Reporte de uso de descuentos
    3. Ver novedades
    0. Salir"""
        )

    else:
        print(
            """\033[1;36m---------------Menu principal Cliente---------------\033[0;m
    1. Buscar descuentos en local
    2. Solicitar descuento
    3. Ver novedades
    0. Salir
    """
        )


def Menu_principal():
    print(
        """
    1. Ingresar con usuario registrado
    2. Registrarse como cliente
    3. Salir
    """
    )


# SECCIÓN DE MENUS # (Final)

""""""
""""""
""""""
""""""
""""""
""""""
""""""

# SECCIÓN DE REGISTRO E INICIO DE SESIÓN # (Inicio)


def pedirusuario():
    global cod
    global eleccion
    global bandera
    global User_g
    contador = 0

    # Ingreso de datos:
    user = input("Escriba su usuario: ").ljust(100, " ")
    contraseña = getpass.getpass("Escriba su contraseña: ").ljust(8, " ")

    pos = Bs_Usu(user)
    if pos != -1:
        ALU.seek(pos, 0)
        cont = pickle.load(ALU)
        if cont.ClaveUsuario == contraseña:
            cod = cont.TipoUsuario.strip()
            User_g = cont.NombreUsuario
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
            pos = Bs_Usu(user)
            if pos != -1:
                ALU.seek(pos, 0)
                cont = pickle.load(ALU)
                if cont.ClaveUsuario == contraseña:
                    cod = cont.TipoUsuario.strip()
                    User_g = cont.NombreUsuario
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


def Registrarse():
    R_Usu.NombreUsuario = input("Ingrese el mail del usuario: ").ljust(100, " ")
    pos = Bs_Usu(R_Usu.NombreUsuario)
    while len(R_Usu.NombreUsuario) <= 100 and pos != -1:
        if pos != -1:
            print("Actualmente ese mail existe, intente con otro...")
        else:
            print("Usted ingreso un mail muy largo, intente otra vez")
        R_Usu.NombreUsuario = input("Ingrese el mail del usuario: ").ljust(100, " ")
        pos = Bs_Usu(R_Usu.NombreUsuario)

    R_Usu.ClaveUsuario = input("Ingrese la clave del usuario: ").ljust(8, " ")
    while len(R_Usu.ClaveUsuario) > 8:
        print("Usted ingreso una clave muy larga, intente otra vez")
        R_Usu.ClaveUsuario = input("Ingrese la clave del usuario: ").ljust(8, " ")

    R_Usu.TipoUsuario = "cliente".ljust(20," ")
    #Buscando el codigo del anterior registro
    ALU.seek(0, 0)
    Aux = pickle.load(ALU)
    T_aux = ALU.tell()
    C_RL = int(os.path.getsize(AFU) / T_aux)
    R_Usu.CodUsuario = C_RL + 1
    C = os.path.getsize(AFU)
    ALU.seek(C, 0)
    pickle.dump(R_Usu, ALU)
    ALU.flush()


# SECCIÓN DE REGISTRO E INICIO DE SESIÓN # (Final)

""""""
""""""
""""""
""""""
""""""
""""""
""""""

# SECCIÓN ADMINISTRADOR CON TODAS SUS SUB-SECCIONES # (Inicio)


def Admin():
    global eleccion
    eleccion = -1
    while eleccion >= -1 and eleccion < 6:
        separador()
        mostrar_menu()
        eleccion = input("Escoger la opción a la que desee acceder: ")

        if (
            eleccion != "1"
            and eleccion != "2"
            and eleccion != "3"
            and eleccion != "4"
            and eleccion != "5"
            and eleccion != "0"
        ):
            os.system("cls")
            print(
                "La opción que has elegido es incorrecta, intentelo de nuevo ingresando un numero del 0 al 5."
            )
            eleccion = -1
        else:
            eleccion = int(eleccion)
            os.system("cls")
            match eleccion:
                case 0:
                    print("\033[3;31mSaliendo del programa...\033[0;m")
                    eleccion = -2
                case 1:
                    gestion_de_locales()
                    eleccion = -1
                case 2:
                    Crear_D()
                case 3:
                    Aprobar()
                case 4:
                    print("Diagramado en chapin")
                case 5:
                    Reporte_A()

def Aprobar():
    cond = Bs_pro_Estado("pendiente".ljust(10," "))
    if cond != -1:
        ALP.seek(0,0)
        R_Pro = pickle.load(ALP)
        TR = ALP.tell()
        T = os.path.getsize(AFP)
        C_RL = T//TR
        ALP.seek(0,0)
        print("Promociones pendientes...")
        while ALP.tell() < T :  
            R_Pro = pickle.load(ALP)
            if R_Pro.Estado.strip() == "pendiente":
                print(R_Pro.CodPromo, R_Pro.TextoPromo.strip(), R_Pro.FechaDesdePromo, R_Pro.FechaHastaPromo, R_Pro.DiaSemana, R_Pro.Estado.strip(), R_Pro.CodLocal)

        rta = Validacion_Promos(0,C_RL,"Ingrese el codigo de promo que desea cambiar (Ingrese 0 si desea salir): " )
        while rta != 0:
            pos = Bs_pro(rta)
            ALP.seek(pos,0)
            R_Pro = pickle.load(ALP)
            if R_Pro.Estado.strip() == "pendiente":
                elec = input("Ingrese `Aprobar` o `Denegar` para aceptar o rechazar la promocion (Ingrese 0 si desea salir): ")
                while elec != "aprobar".lower() and elec != "Denegar".lower() and elec != "0":
                    separador()
                    print("Usted ingreso un valor no aceptado, intente nuevamente...")
                    elec = input("Ingrese `Aprobar` o `Denegar` para aceptar o rechazar la promocion (Ingrese 0 si desea salir): ")
                if elec.lower() == "aprobar":
                    ALP.seek(pos,0)
                    R_Pro.Estado = "aprobada".ljust(10," ")
                    pickle.dump(R_Pro, ALP)
                    ALP.flush()
                elif elec.lower() == "denegar":
                    ALP.seek(pos,0)
                    R_Pro.Estado = "rechazada".ljust(10," ")
                    pickle.dump(R_Pro,ALP)
                    ALP.flush()      
            else:
                print("La promoción no se encuentra en estado pendiente")
            rta = Validacion_Promos(0,C_RL,"Ingrese el codigo de promo que desea cambiar (Ingrese 0 si desea salir): " )
    else:
        print("No hay promociones en estado pendiente")
    
def Crear_D():
    R_Usu.NombreUsuario = input("Ingrese el mail del usuario: ").ljust(100, " ")
    pos = Bs_Usu(R_Usu.NombreUsuario)
    while len(R_Usu.NombreUsuario) <= 100 and pos != -1:
        if pos != -1:
            print("Actualmente ese mail existe, intente con otro...")
        else:
            print("Usted ingreso un mail muy largo, intente otra vez")
        R_Usu.NombreUsuario = input("Ingrese el mail del usuario: ").ljust(100, " ")
        pos = Bs_Usu(R_Usu.NombreUsuario)

    R_Usu.ClaveUsuario = input("Ingrese la clave del usuario: ").ljust(8, " ")
    while len(R_Usu.ClaveUsuario) > 8:
        print("Usted ingreso una clave muy larga, intente otra vez")
        R_Usu.ClaveUsuario = input("Ingrese la clave del usuario: ").ljust(8, " ")

    R_Usu.TipoUsuario = "dueño de local".ljust(20," ")
    #Buscando el codigo del anterior registro
    ALU.seek(0, 0)
    Aux = pickle.load(ALU)
    T_aux = ALU.tell()
    C_RL = int(os.path.getsize(AFU) / T_aux)
    R_Usu.CodUsuario = C_RL + 1
    C = os.path.getsize(AFU)
    ALU.seek(C, 0)
    pickle.dump(R_Usu, ALU)
    ALU.flush()

def gestion_de_locales():
    global eleccion
    global decision
    if Bs_Usu_Tipo("dueño de local".ljust(20," ")) != -1:
        while (
            decision != "a"
            and decision != "b"
            and decision != "c"
            and decision != "d"
            and eleccion == 1
        ):
            mostrar_menu()
            decision = input("Escoger la opción a la que desee acceder: ")

            os.system("cls")

            if (
                decision != "a"
                and decision != "b"
                and decision != "c"
                and decision != "d"
                and decision != "e"
            ):
                separador()
                print(
                    "La opción que has elegido es incorrecta, intentelo de nuevo ingresando una de las letras dadas."
                )

            elif decision == "a":
                os.system("cls")
                locales_cargados = input(
                    "¿Desea ver los locales cargados hasta el momento?(Si o No): "
                )
                while (
                    locales_cargados.lower() != "si"
                    and locales_cargados.lower() != "no"
                ):
                    print("Necesitamos que responda con un Si o No, para continuar")
                    locales_cargados = input(
                        "¿Desea ver los locales cargados hasta el momento?(Si o No): "
                    )
                if locales_cargados.lower() == "si":
                    Exhibicion()
                separador()
                Crear_Locales()
                separador()
                decision = "z"

            # Nuevo, revisar.
            elif decision == "b":
                os.system("cls")
                locales_cargados = input(
                    "¿Desea ver los locales cargados hasta el momento?(Si o No): "
                )
                while (
                    locales_cargados.lower() != "si"
                    and locales_cargados.lower() != "no"
                ):
                    print("Necesitamos que responda con un Si o No, para continuar")
                    locales_cargados = input(
                        "¿Desea ver los locales cargados hasta el momento?(Si o No): "
                    )
                if locales_cargados.lower() == "si":
                    Exhibicion()
                separador()
                Modificar_Locales()
                decision = "z"

            # Nuevo, revisar.
            elif decision == "c":
                os.system("cls")
                locales_cargados = input(
                    "¿Desea ver los locales cargados hasta el momento?(Si o No): "
                )
                while (
                    locales_cargados.lower() != "si"
                    and locales_cargados.lower() != "no"
                ):
                    print("Necesitamos que responda con un Si o No, para continuar")
                    locales_cargados = input(
                        "¿Desea ver los locales cargados hasta el momento?(Si o No): "
                    )
                if locales_cargados.lower() == "si":
                    Exhibicion()
                separador()
                Eliminar_Locales()
                decision = "z"

            # Falta desarrollar
            elif decision == "d":
                os.system("cls")
                Mapa_Locales()
                decision = "z"

            elif decision == "e":
                eleccion = -1
                decision = "z"
    else:
        print("No hay dueños de locales cargados hasta el momento.")

def Crear_Locales():
    #Auxiliares para guardar cantidades
    guard_cant0 = 0 
    guard_cant1 = 0
    guard_cant2 = 0
    verificacion = -2
    nombre = input(
        "Ingrese el nombre del local (si no quiere crear locales ingrese 0): "
    )
    nombre = nombre.lower()

    while len(nombre) > 30:
        print("Usted ingreso un nombre muy largo... ")
        separador()
        nombre = input(
            "Ingrese un nombre mas corto (si no quiere crear locales ingrese 0): "
        )
        nombre = nombre.lower()

    while nombre != "0":
        # Verificación y carga del nombre:
        while verificacion != -1 and nombre != "0":
            if os.path.getsize(AFL) != 0:
                verificacion = Bd_archivo(nombre)
                if verificacion != -1:
                    print("Usted ingreso un nombre ya existente")
                    separador()
                    nombre = input(
                        "Ingrese otro nombre de local (si no quiere crear locales ingrese 0): "
                    )
                    nombre = nombre.lower()
            else:
                verificacion = -1
        verificacion = -2
        if nombre != "0":
            # Cargando Ubicación:
            Ubi = input("Ingrese la ubicación para el local: ")
            while len(Ubi) > 30:
                print("Usted ingreso una ubicación muy larga... ")
                separador()
                Ubi = input("Ingrese una ubicación mas corta: ")
            # Cargando Rubro:
            rubro = input(
                "Ingrese el tipo de rubro del local (perfumería, comida o indumentaria): "
            )
            rubro = rubro.lower()

            # Verificacíon y carga del rubro
            while ( rubro != "perfumeria" and
                rubro != "perfumería"
                and rubro != "indumentaria"
                and rubro != "comida"
            ):
                print(
                    "Usted no ingreso los datos correctamente porfavor intentelo otra vez..."
                )
                separador()
                rubro = input(
                    "Ingrese el tipo de rubro del local (perfumería, comida o indumentaria): "
                )
                rubro = rubro.lower()
            if rubro == "perfumeria" or rubro == "perfumería":
                Rubros[0].Ca = Rubros[0].Ca + 1
            elif rubro == "indumentaria":
                Rubros[1].Ca = Rubros[1].Ca + 1
            else:
                Rubros[2].Ca = 1 + Rubros[2].Ca
            
            # Pidiendo el Código de usuario
            flag = 0
            Cod_us = input("Ingrese el codigo de usuario: ")
            if Cod_us.isdigit():
                Cod_us = int(Cod_us)
                Veri = Bs_Usu_Cod(Cod_us)
                if Veri != -1:
                    ALU.seek(Veri, 0)
                    R_Usu = pickle.load(ALU)
                    if R_Usu.TipoUsuario.strip() == "dueño de local":
                        flag = 1
            while flag == 0:
                print("Usted ingreso un codigo de usuario erroneo, intentelo de nuevo")
                separador()
                Cod_us = input("Ingrese el codigo de usuario: ")
                if Cod_us.isdigit():
                    Cod_us = int(Cod_us)
                    Veri = Bs_Usu_Cod(Cod_us)
                    if Veri != -1:
                        ALU.seek(Veri, 0)
                        R_Usu = pickle.load(ALU)
                        if R_Usu.TipoUsuario.strip() == "dueño de local":
                            flag = 1

            #Buscando el codigo del local del anterior registro
            if os.path.getsize(AFL) > 0:
                ALL.seek(0, 0)
                Aux_I = pickle.load(ALL)
                T_AL = os.path.getsize(AFL)
                T_aux = ALL.tell()
                C_RL = round(T_AL / T_aux)
                Cod_ant = C_RL
            else:
                Cod_ant = 0
            # Cargando registro locales.
            M = os.path.getsize(AFL)
            print("Tamaño del archivo: ", M)
            ALL.seek(M, 0)
            R_Loc.CodLocal = Cod_ant + 1
            R_Loc.NombreLocal = nombre.ljust(30," ")
            R_Loc.UbiLocal = Ubi.ljust(30," ")
            R_Loc.RubroLocal = rubro.ljust(12," ")
            R_Loc.CodUsuario = Cod_us
            R_Loc.Estado = "A"
            pickle.dump(R_Loc, ALL)
            ALL.flush()
            separador()
            or_archivo()
            # Pidiendo el siguiente local
            nombre = input(
                "Ingrese el nombre del local (si no quiere crear locales ingrese 0): "
            )
            nombre = nombre.lower()
    
    guard_cant0  = Rubros[0].Ca
    guard_cant1 = Rubros[1].Ca
    guard_cant2  = Rubros[2].Ca

    os.system("cls")
    # Ordenando array de rubros y cantidades (de mayor a menor)
    for i in range(0, 2):
        for j in range(i + 1, 3):
            if Rubros[i].Ca < Rubros[j].Ca:
                # Ordenando arreglo de cantidades
                aux = Rubros[i].Ca
                Rubros[i].Ca = Rubros[j].Ca
                Rubros[j].Ca = aux
                # Ordenando arreglo de rubros
                aux1 = Rubros[i].Nom.ljust(12," ")
                Rubros[i].Nom = Rubros[j].Nom.ljust(12," ")
                Rubros[j].Nom = aux1
    os.system("cls")
    borde = "║"
    label1 = "║    Rubro   "
    label1 += borde
    label1 += "Cantidad de Locales"
    label1 += borde
    sys.stdout.write("╔")
    sys.stdout.write(12 * "═")
    sys.stdout.write("╦")
    sys.stdout.write(19 * "═")
    sys.stdout.write("╗\n")
    print(label1)
    for i in range(0, 3):
        sys.stdout.write("╠")
        sys.stdout.write(12 * "═")
        sys.stdout.write("╬")
        sys.stdout.write(19 * "═")
        sys.stdout.write("╣\n")
        item = ""
        item += "║"
        item += str(Rubros[i].Nom).strip().center(12)
        item += borde
        item += str(Rubros[i].Ca).center(19)
        item += "║"
        print(item)
    sys.stdout.write("╚")
    sys.stdout.write(12 * "═")
    sys.stdout.write("╩")
    sys.stdout.write(19 * "═")
    sys.stdout.write("╝\n")

    Rubros[0].Nom = "perfumeria".ljust(12," ")
    Rubros[1].Nom = "indumentaria".ljust(12," ")    
    Rubros[2].Nom = "comida".ljust(12," ")
    Rubros[0].Ca = guard_cant0
    Rubros[1].Ca = guard_cant1
    Rubros[2].Ca = guard_cant2

def Modificar_Locales():
    # Procedimiento para la modificación de un local:
    def Modificacion(pos_reg):
        verificacion = -2
        print("Aclaración: si no desea modificar ninguna parte ingrese 0")
        modif = input(
            "Que parte del local desea modificar(nombre, ubicación, rubro o codigo de usuario)? "
        )
        modif = modif.lower()
        separador()
        while (
            modif != "nombre"
            and modif != "ubicacion"
            and modif != "ubicación"
            and modif != "rubro"
            and modif != "codigo de usuario"
            and modif != "0"
        ):
            print("Usted ingreso un valor no valido, intentelo de nuevo")
            separador()
            modif = input(
                "Que parte del local desea modificar(nombre, ubicación, rubro o codigo de usuario)? "
            )
            modif = modif.lower()

        # Modificación del nombre:
        if modif == "nombre":
            nombre = input("Ingrese otro nombre para el local: ")
            nombre = nombre.lower()
            while len(nombre) > 30:
                print("Usted ingreso un nombre muy largo... ")
                separador()
                nombre = input("Ingrese un nombre mas corto: ")
                nombre = nombre.lower()

            while verificacion != -1:
                verificacion = Bd_archivo(nombre)
                if verificacion == -1:
                    print("Nombre correcto.")
                else:
                    print("Usted ingreso un nombre ya existente")
                    separador()
                    nombre = input(
                        "Ingrese otro nombre de local (si no quiere crear locales ingrese 0): "
                    )
                    nombre = nombre.lower()
            verificacion = -2
            ALL.seek(pos_reg, 0)
            R_Loc = pickle.load(ALL)
            R_Loc.NombreLocal = nombre.ljust(30," ")
            print("Su modificación se a realizado con exito")

        # Modificación de la ubicación:
        elif modif == "ubicacion" or modif == "ubicación":
            Ubi = input("Ingrese la nueva ubicación para el local: ")
            while len(Ubi) > 30:
                print("Usted ingreso una ubicación muy larga... ")
                separador()
                Ubi = input("Ingrese una ubicación mas corta: ")
            ALL.seek(pos_reg, 0)
            R_Loc = pickle.load(ALL)
            R_Loc.UbiLocal = Ubi.ljust(30," ")
            print("Su modificación se a realizado con exito")

        # Modificación del rubro
        elif modif == "rubro":
            rubro = input(
                "Ingrese el nuevo rubro (perfumería, comida o indumentaria): "
            )
            rubro = rubro.lower()
            while ( rubro != "perfumeria"and
                rubro != "perfumería"
                and rubro != "indumentaria"
                and rubro != "comida"
            ):
                print(
                    "Usted no ingreso los datos correctamente, porfavor intentelo otra vez"
                )
                separador()
                rubro = input(
                    "Ingrese el nuevo rubro del local (perfumería, comida o indumentaria): "
                )
                rubro = rubro.lower()
            ALL.seek(pos_reg, 0)
            R_Loc = pickle.load(ALL)    
            tipo = R_Loc.RubroLocal.ljust(12," ")
            #Buscando el anterior rubro
            c = 0
            while Rubros[c].Nom != tipo:
                c = c + 1
            Rubros[c].Ca = Rubros[c].Ca - 1
            #Buscando el nuevo rubro
            c1 = 0
            while Rubros[c1].Nom.strip() != rubro:
                c1 = c1 + 1
            Rubros[c1].Ca = Rubros[c1].Ca + 1
            R_Loc.RubroLocal = rubro.ljust(12," ")
            print("Su modificación se a realizado con exito")

        # Modificación del código de usuario
        elif modif == "codigo de usuario":
            flag = 0
            Cod_us = input("Ingrese el codigo de usuario: ")
            if Cod_us.isdigit():
                Cod_us = int(Cod_us)
                Veri = Bs_Usu_Cod(Cod_us)
                if Veri != -1:
                    ALL.seek(Veri, 0)
                    R_Usu = pickle.load(ALU)
                    if R_Usu.TipoUsuario.strip() == "dueño de local":
                        flag = 1
            while flag == 0:
                print("Usted ingreso un codigo de usuario erroneo, intentelo de nuevo")
                separador()
                Cod_us = input("Ingrese el codigo de usuario: ")
                if Cod_us.isdigit():
                    Cod_us = int(Cod_us)
                    Veri = Bs_Usu_Cod(Cod_us)
                    if Veri != -1:
                        ALL.seek(Veri, 0)
                        R_Usu = pickle.load(ALU)
                        if R_Usu.TipoUsuario.strip() == "dueños de local":
                            flag = 1
            ALL.seek(pos_reg, 0)
            R_Loc = pickle.load(ALL)
            R_Loc.CodUsuario = Cod_us
            print("Su modificación se a realizado con exito")
        else:
            print("No se realizó ninguna modificación")

        if modif != "0":
            # Cargando al archivo
            ALL.seek(pos_reg, 0)
            pickle.dump(R_Loc, ALL)
            ALL.flush()

    cod_local = input(
        "Ingrese el codigo del local que desea modificar(si no desea modificar ninguno ingrese 0): "
    )
    while cod_local != "0":
        if cod_local.isdigit():
            cod_local = int(cod_local)
            pos = Bs_Loc(cod_local)
            if pos == -1:
                print("Usted ingreso un valor no valido, intentelo de nuevo")
                separador()
                cod_local = input(
                    "Ingrese el codigo del local que desea modificar(si no desea modificar ninguno ingrese 0): "
                )
            else:
                print("Local encontrado!!!")
                ALL.seek(pos, 0)
                R_Loc = pickle.load(ALL)
                if R_Loc.Estado == "B":
                    print("Este local esta dado de baja")
                    rta = input("Desea cambiarlo a estado activo? (si o no): ")
                    while rta != "si" and rta != "no":
                        print("Porfavor seleccione si o no...")
                        rta = input("Desea cambiarlo a estado activo? (si o no): ")
                        rta = rta.lower
                    if rta == "no":
                        separador()
                        cod_local = input(
                            "Ingrese el codigo de otro local que desee modificar(si no desea modificar ninguno ingrese 0): "
                        )
                    else:       
                        ALL.seek(pos, 0)
                        R_Loc = pickle.load(ALL)
                        R_Loc.Estado = "A"
                        ALL.seek(pos, 0)
                        pickle.dump(R_Loc, ALL)
                        ALL.flush()
                            
                        tipo = R_Loc.RubroLocal.ljust(12," ")
                        #Buscando el anterior rubro
                        c = 0
                        while Rubros[c].Nom != tipo:
                            c = c + 1
                        Rubros[c].Ca = Rubros[c].Ca + 1

                        Modificacion(pos)
                        separador()
                        Exhibicion()
                        cod_local = input(
                            "Ingrese el siguiente codigo del local que desea modificar(si no desea modificar ninguno ingrese 0): "
                        )
                else:
                    Modificacion(pos)
                    separador()
                    Exhibicion()
                    cod_local = input(
                        "Ingrese el siguiente codigo del local que desea modificar(si no desea modificar ninguno ingrese 0): "
                    )
        else:
            print("Usted ingreso un valor no valido, intentelo de nuevo")
            separador()
            cod_local = input(
                "Ingrese el codigo del local que desea modificar(si no desea modificar ninguno ingrese 0): "
            )

def Eliminar_Locales():
    eliminar = input(
        "Ingrese el codigo del local que desea eliminar(si no desea eliminar ninguno ingrese 0): "
    )
    while eliminar != "0":
        if eliminar.isdigit():
            eliminar = int(eliminar)
            pos = Bs_Loc(eliminar)
            if pos == -1:
                print("Usted ingreso un valor no valido, intentelo de nuevo")
                separador()
                eliminar = input(
                    "Ingrese el codigo del local que desea eliminar(si no desea modificar ninguno ingrese 0): "
                )
            else:
                print("Local encontrado!!!")
                ALL.seek(pos, 0)
                R_Loc = pickle.load(ALL)
                if R_Loc.Estado == "B":
                    print("Este local esta dado de baja")
                    eliminar = input(
                        "Ingrese otro codigo del local que desee eliminar(si no desea eliminar ninguno ingrese 0): "
                    )
                else:
                    confirmacion = input(
                        "Desea confirmar la eliminación de este local? (si o no): "
                    )
                    while confirmacion != "si" and confirmacion != "no":
                        print("Porfavor seleccione si o no...")
                        confirmacion = input(
                            "Desea confirmar la eliminación de este local? (si o no): "
                        )
                    if confirmacion == "no":
                        separador()
                        eliminar = input(
                            "Ingrese otro codigo del local que desee eliminar(si no desea eliminar ninguno ingrese 0): "
                        )
                    else:
                        tipo = R_Loc.RubroLocal.ljust(12," ")
                        #Buscando el anterior rubro
                        c = 0
                        while Rubros[c].Nom != tipo:
                            c = c + 1
                        Rubros[c].Ca = Rubros[c].Ca - 1
                        ALL.seek(pos, 0)
                        R_Loc.Estado = "B"
                        pickle.dump(R_Loc, ALL)
                        ALL.flush()
                        os.system("cls")
                        print("El local ha sido eliminado...")
                        separador()
                        Exhibicion()
                        eliminar = input(
                            "Ingrese el siguiente codigo del local que desee eliminar(si no desea eliminar ninguno ingrese 0): "
                        )
        else:
            print("Usted ingreso un valor no valido, intentelo de nuevo")
            separador()
            eliminar = input(
                "Ingrese el codigo del local que desea eliminar(si no desea eliminar ninguno ingrese 0): "
            )

def Mapa_Locales():
    os.system("cls")
    print(
        """
        Referencias: 
        - \033[0;32mLocal activo\033[0;m
        - \033[0;31mLocal inactivo\033[0;m
        """
    )
    print("                 Mapa de Locales")
    print("", "+--------+--------+--------+--------+--------+")
    ALL.seek(0, 0)
    for i in range(0, 10):
        for j in range(0, 5):
            try:
                R_Loc = pickle.load(ALL)
                T = os.path.getsize(AFL)
                if ALL.tell() <= T and R_Loc.Estado == "A":
                    Codigo = f"\033[1;32m{R_Loc.CodLocal}\033[0;m"
                elif ALL.tell() <= T and R_Loc.Estado == "B":
                    Codigo = f"\033[1;31m{R_Loc.CodLocal}\033[0;m"
            except:
                Codigo = 0
            sys.stdout.write(f" |   {Codigo}   ")
        print(" |  \n +--------+--------+--------+--------+--------+")

def Reporte_A():
    ALL.seek(0,0)
    ALU.seek(0,0)
    ALP.seek(0,0)
    TL = os.path.getsize(AFL)
    aux_l = pickle.load(ALL)
    pos_L = ALL.tell()
    C_R = round(TL/pos_L)
    TP = os.path.getsize(AFP)
    Aux = pickle.load(ALP)
    pos_P = ALP.tell()
    C_RP = round(TP/pos_P)
    T = os.path.getsize(AFU)
    aux = pickle.load(ALU)
    pos = ALU.tell()
    C_RU = round(T/pos)
    ALU.seek(0,0)
    if TP != 0:
        while ALU.tell() < T:
            R_Usu = pickle.load(ALU)
            ALL.seek(0,0)
            for i in range(0,C_R):
                R_Loc = pickle.load(ALL)
                if R_Usu.CodUsuario == R_Loc.CodUsuario:
                    ALP.seek(0,0)
                    for j in range(0, C_RP):
                        R_Pro = pickle.load(ALP)
                        if R_Pro.CodLocal == R_Loc.CodLocal and R_Pro.Estado.strip() == "aprobada":
                            Usos = Conteo_Usos(R_Pro.CodPromo)
                            separador()
                            print(f"El dueño: {R_Usu.NombreUsuario.strip()}, Tiene las siguientes promos en el codigo de local {R_Loc.CodLocal}")
                            print(f"La promo es: {R_Pro.TextoPromo.strip()}, los dias disponibles son: {R_Pro.DiaSemana}")
                            print(f"Se uso una cantidad de {Usos}")
                        
        input("")                  
                
                #FALTA PONERLA DE FORMA AESTETHIC
            
    else:
        print("No hay promociones disponibles")
        


# SECCIÓN ADMINISTRADOR CON TODAS SUS SUB-SECCIONES # (Final)

""""""
""""""
""""""
""""""
""""""
""""""
""""""

# SECCION  DUEÑOS DE LOCALES CON TODAS SUS SUB-SECCIONES # (Inicio)


def DueñoDelocales():
    global eleccion
    eleccion = -1
    while eleccion >= -1 and eleccion < 4:
        separador()
        mostrar_menu()
        eleccion = input("Escoger la opción a la que desee acceder: ")

        if (
            eleccion != "1"
            and eleccion != "2"
            and eleccion != "3"
            and eleccion != "0"
        ):
            os.system("cls")
            print(
                "La opción que has elegido es incorrecta, intentelo de nuevo ingresando un numero del 0 al 3."
            )
            eleccion = -1
        else:
            eleccion = int(eleccion)
            os.system("cls")
            match eleccion:
                case 0:
                    print("\033[3;31mSaliendo del programa...\033[0;m")
                    eleccion = -2
                case 1:
                    Crear_Descuentos()
                    eleccion = -1
                case 2:
                    Reporte()
                case 3:
                    Aprobar()


def Crear_Descuentos():
    global User_g, R_Pro
    pos = Bs_Usu(User_g)
    ALU.seek(pos, 0)
    R_Usu = pickle.load(ALU)
    ALL.seek(0, 0)
    #Listado
    if os.path.getsize(AFP) != 0:
      while ALL.tell() < os.path.getsize(AFL):
        R_Loc = pickle.load(ALL)
        if R_Loc.Estado == "A" and R_Usu.CodUsuario == R_Loc.CodUsuario:
            print(f"El local {R_Loc.NombreLocal.strip()} tiene las siguientes promociones: ")
            ALP.seek(0,0)
            while ALP.tell() < os.path.getsize(AFP):
              R_Pro = pickle.load(ALP)
              if R_Loc.CodLocal == R_Pro.CodLocal and R_Pro.FechaDesdePromo <= datetime.date.today() and R_Pro.FechaHastaPromo >= datetime.date.today():
                  print(f"-Promición {R_Pro.TextoPromo.strip()} tiene un Estado: {R_Pro.Estado}")
                  separador()
    else:
      print("Aún no hay promociones cargadas. ")
    if os.path.getsize(AFL) != 0:
      ALL.seek(0, 0)
      R_Loc = pickle.load(ALL)
      T_R = ALL.tell()
      Cant_R = os.path.getsize(AFL) // T_R
      Exhibicion()
      print("Aviso: Ingrese 0 si desea salir")
      Cod_Loc = Validacion(0, Cant_R,"Ingrese el código del local al que le quiere asignar una promoción")
      if Cod_Loc != 0:
            pos = Bs_Loc(Cod_Loc)
            ALL.seek(pos, 0)
            R_Loc = pickle.load(ALL)
            while R_Usu.CodUsuario != R_Loc.CodUsuario:
              os.system("cls")
              print("El local no pertenece a este dueño.")
              separador()
              print("Aviso: Ingrese 0 si desea salir")
              Cod_Loc = Validacion(0, Cant_R,"Ingrese el código del local al que le quiere asignar una promoción")
              if Cod_Loc != 0:
                  pos = Bs_Loc(Cod_Loc)
                  ALL.seek(pos, 0)
                  R_Loc = pickle.load(ALL)
            if os.path.getsize(AFP) > 0:
                      ALP.seek(0, 0)
                      Aux_I = pickle.load(ALP)
                      T_AP = os.path.getsize(AFP)
                      T_aux = ALP.tell()
                      C_RP = round(T_AP / T_aux)
                      Cod_ant = C_RP
            else:
                      Cod_ant = 0
            ALP.seek(0, 2)
            R_Pro.CodPromo = Cod_ant + 1
            R_Pro.TextoPromo = input("Ingrese la descripción de la promoción(Max 30 caracteres): ").ljust(200," ") #Máximo ideal 200, 30 es lo conveniente para mostrarlo en cuadro
            while len(R_Pro.TextoPromo.strip()) > 30:
              print("Usted ingreso una descripción muy larga... ")
              separador()
              R_Pro.TextoPromo  = input("Ingrese la descripción de la promoción(Max 30 caracteres): ") #Máximo ideal 200, 30 es lo conveniente para mostrarlo en cuadro
            R_Pro.FechaDesdePromo  = Validacion_fecha_Desde()
            print("Por favor ingresa la fecha de fin de la promoción: ")
            R_Pro.FechaHastaPromo = Validacion_fecha()
            while R_Pro.FechaDesdePromo > R_Pro.FechaHastaPromo:
                print("Por favor ingresa la fecha de fin de la promoción: ")
                R_Pro.FechaHastaPromo = Validacion_fecha()
            print("Ingrese los días de semana en los cuales la promoción es válida con 1, si no ingrese 0: ")
            for i in range(0,7):
              R_Pro.DiaSemana[i] = Validacion(0,1,f"Día de la semana {i}: ")
            R_Pro.Estado = "pendiente".ljust(10," ")
            R_Pro.CodLocal = Cod_Loc
            pickle.dump(R_Pro, ALP)
            ALP.flush()
    else:
        print("Aun no hay, por ende no se pueden crear promociones. ")


def Reporte():
   if os.path.getsize(AFP) != 0:
        global User_g
        pos = Bs_Usu(User_g)
        ALU.seek(pos, 0)
        R_Usu = pickle.load(ALU)

        Fecha_d = Validacion_RangoI_Reporte()
        Fecha_h = Validacion_RangoF_Reporte(Fecha_d)

        os.system("cls")
        print(f"Reporte de uso de descuentos del dueño: {R_Usu.NombreUsuario}")
        print(f"Fecha desde: {Fecha_d}              Fecha hasta: {Fecha_h}")
        ALL.seek(0,0)
        while ALL.tell() < os.path.getsize(AFL):
            R_Loc = pickle.load(ALL)
            if R_Usu.CodUsuario == R_Loc.CodUsuario: 
                print(f"Local {R_Loc.CodLocal}: {R_Loc.NombreLocal}")
                Exhibicion_Reportes(Fecha_d,Fecha_h, R_Loc.CodLocal)
                print("\n") 

def Ver_Nov():
    print("Diagramado en chapin")


# SECCION  DUEÑOS DE LOCALES CON TODAS SUS SUB-SECCIONES # (Final)

""""""
""""""
""""""
""""""
""""""
""""""
""""""

# SECCION  CLIENTES CON TODAS SUS SUB-SECCIONES # (Inicio)


def Clientes():
  global eleccion 
  eleccion = -1 
  while eleccion >= -1 and eleccion <= 3:
      separador()
      mostrar_menu()
      eleccion = Validacion(0,3,"Ingrese una opción")
      match eleccion:
          case 0:
              eleccion = -2
          case 1: 
              Bus_Desc()
          case 2:
              Solic_Desc()
          case 3:
              print("Esta sección esta diagramada en chapin")

def Bus_Desc():
  if os.path.getsize(AFP) != 0:
    ALL.seek(0,0)
    R_Loc = pickle.load(ALL)
    T_R = ALL.tell()
    Cant_R = os.path.getsize(AFL)//T_R
    Exhibicion()
    Cod_local = Validacion_Clientes(0,Cant_R,"Ingrese un código de local")
    Fecha = Validacion_fecha()
    Exhibicion_Clientes(Cod_local,Fecha)
  else:
    print("Aún no hay ninguna promoción cargada.")

def Solic_Desc():
  global User_g
  if os.path.getsize(AFP) != 0:
    ALP.seek(0,0)
    R_Pro = pickle.load(ALP)
    T_R = ALP.tell()
    Tam = os.path.getsize(AFP)
    Cant_R = Tam//T_R
    Exhibicion_Clientes_Desc()
    Cod_pro = Validacion(0,Cant_R,"Ingrese el código de la promoción que desea usar: ")
    Fecha = datetime.datetime.now().date()
    Pos = Bs_pro(Cod_pro)
    ALP.seek(Pos, 0)
    R_Pro = pickle.load(ALP)
    if R_Pro.CodPromo == Cod_pro and R_Pro.Estado.strip() == "aprobada" and R_Pro.FechaDesdePromo <= Fecha and R_Pro.FechaHastaPromo >= Fecha:
      if R_Pro.DiaSemana[Fecha.weekday()] == 1:
            pos = Bs_Usu(User_g)
            ALU.seek(pos, 0)
            R_Usu = pickle.load(ALU)
            R_Uso_Pro.CodCliente = R_Usu.CodUsuario
            R_Uso_Pro.CodPromo = Cod_pro
            R_Uso_Pro.FechaUsoPromo = Fecha 
            ALUP.seek(0,2)
            pickle.dump(R_Uso_Pro,ALUP)
            ALUP.flush()
            print("Promoción utilizada correctamente")
      else:
          print("La promoción no esta activa este dia")
  else:
    print("Aún no hay ninguna promoción cargada.")


# SECCION  CLIENTES CON TODAS SUS SUB-SECCIONES # (Final)

""""""
""""""
""""""
""""""
""""""
""""""
""""""

# Declaración de variables...
eleccion = -1
decision = ""
bandera = 0
i_global = 1 #Eliminar una vez modificado el arreglo de rubros y cantidades
frenar = True
User_g = ""



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
    R_Usu.CodUsuario = 1
    R_Usu.NombreUsuario = "admin".ljust(100, " ")
    R_Usu.ClaveUsuario = "12345".ljust(8, " ")
    R_Usu.TipoUsuario = "administrador".ljust(20, " ")
    ALU.seek(0, 2)
    pickle.dump(R_Usu, ALU)
    ALU.flush()


# PROGRAMA PRINCIPAL #

os.system("cls")
Menu_principal()
Eleccion = Validacion(1, 3,"Ingrese una opción")
while Eleccion != 3:
    if Eleccion == 1:
        pedirusuario()
        match cod.strip():
            case "administrador":
                if os.path.getsize(AFL) > 0: #Ayuda para entender todo sobre los registros
                    separador()
                    ALL.seek(0, 0)
                    Aux = pickle.load(ALL)
                    T_aux = ALL.tell()
                    C_RL = int(os.path.getsize(AFL) / T_aux)
                    print("Tamaño del archivo: ", os.path.getsize(AFL))
                    print("Tamaño de cada registro: ", T_aux)
                    print("Cantidad de Registros: ", C_RL)
                    if C_RL > 2:
                        Aux = pickle.load(ALL)
                        T_aux_2 = ALL.tell()
                        print("Tamaño de 2 registros: ", T_aux_2)
                        ALL.seek(-T_aux_2, 1)
                        Aux = pickle.load(ALL)
                    separador()
                Admin()
            case "dueño de local":
                DueñoDelocales()
            case "cliente":
                Clientes()
    elif Eleccion == 2:
        Registrarse()
    else:
        print("Hasta luego...")
        bandera = -1
    os.system("cls")
    Menu_principal()
    Eleccion = Validacion(1, 3,"Ingrese una opción")
