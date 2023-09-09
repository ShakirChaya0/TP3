import getpass
import pickle
import os.path
import os
import sys
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


Rubros = [0] * 3
Rubros[0] = "perfumeria"
Rubros[1] = "indumentaria"
Rubros[2] = "comida"

Rubros_c = [0] * 3

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
            item += Auxiliar.RubroLocal.center(12)
            item += borde
            item += Auxiliar.Estado.center(6)
            item += "║"
            i += 1
            ALL.seek((i * T_RL) +10 , 0)
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
    while inf < sup and R_L.NombreLocal != X:
        if X < R_L.NombreLocal:
            sup = medio - 1
        else:
            inf = medio + 1
        medio = (inf + sup) // 2
        if medio >= 0:
            ALL.seek(medio * T_RL, 0)
            R_L = pickle.load(ALL)
    if R_L.NombreLocal == X:
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


def Validacion(desde, hasta):
    while True:
        try:
            numero = int(
                input(f"Por favor ingresa una opción, número entre {desde} y {hasta}: ")
            )
            if desde <= numero <= hasta:
                return numero
            else:
                print(
                    f"El número debe estar entre {desde} y {hasta}. Inténtalo de nuevo."
                )
        except ValueError:
            print("¡Eso no es un número válido! Inténtalo de nuevo.")


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
    global i_usu
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

    R_Usu.TipoUsuario = "cliente"
    R_Usu.CodUsuario = i_usu
    i_usu = i_usu + 1
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
                    Reporte()


def Reporte():
    print("a")


def Aprobar():
    print("a")


def Crear_D():
    global i_usu
    global cond_crear
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

    R_Usu.TipoUsuario = "dueño de local"
    R_Usu.CodUsuario = i_usu
    i_usu = i_usu + 1
    C = os.path.getsize(AFU)
    ALU.seek(C, 0)
    pickle.dump(R_Usu, ALU)
    ALU.flush()
    cond_crear = 1


def gestion_de_locales():
    global eleccion
    global decision
    if Bs_Usu_Tipo("dueño de local") != -1:
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
    global i_global
    global cond_crear
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
            while (
                rubro != "perfumeria"
                and rubro != "perfumería"
                and rubro != "indumentaria"
                and rubro != "comida"
            ):
                print(
                    "Usted no ingreso los datos correctamente porfavor intentelo otra vez..."
                )
                separador()
                rubro = input(
                    "Ingrese el tipo de rubro del local (perfumeria, comida o indumentaria): "
                )
                rubro = rubro.lower()
            pos_suma = Bs_Sec_R(Rubros[:], rubro)
            if rubro == "perfumeria" or rubro == "perfumería":
                Rubros_c[pos_suma] = Rubros_c[pos_suma] + 1
            elif rubro == "indumentaria":
                Rubros_c[pos_suma] = Rubros_c[pos_suma] + 1
            else:
                Rubros_c[pos_suma] = Rubros_c[pos_suma] + 1
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

            # Cargando registro locales.
            M = os.path.getsize(AFL)
            ALL.seek(M, 0)
            R_Loc.CodLocal = i_global
            R_Loc.NombreLocal = nombre
            R_Loc.UbiLocal = Ubi
            R_Loc.RubroLocal = rubro
            R_Loc.CodUsuario = Cod_us
            R_Loc.Estado = "A"
            pickle.dump(R_Loc, ALL)
            ALL.flush()
            # Aumentando el contador global post carga de un local
            i_global = i_global + 1
            separador()
            or_archivo()
            # Pidiendo el siguiente local
            nombre = input(
                "Ingrese el nombre del local (si no quiere crear locales ingrese 0): "
            )
            nombre = nombre.lower()

    os.system("cls")
    # Ordenando array de rubros y cantidades (de mayor a menor)
    for i in range(0, 2):
        for j in range(i + 1, 3):
            if Rubros_c[i] < Rubros_c[j]:
                # Ordenando arreglo de cantidades
                aux = Rubros_c[i]
                Rubros_c[i] = Rubros_c[j]
                Rubros_c[j] = aux
                # Ordenando arreglo de rubros
                aux1 = Rubros[i]
                Rubros[i] = Rubros[j]
                Rubros[j] = aux1
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
        item += str(Rubros[i]).center(12)
        item += borde
        item += str(Rubros_c[i]).center(19)
        item += "║"
        print(item)
    sys.stdout.write("╚")
    sys.stdout.write(12 * "═")
    sys.stdout.write("╩")
    sys.stdout.write(19 * "═")
    sys.stdout.write("╝\n")


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
            R_Loc.NombreLocal = nombre
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
            R_Loc.UbiLocal = Ubi
            print("Su modificación se a realizado con exito")

        # Modificación del rubro
        elif modif == "rubro":
            rubro = input(
                "Ingrese el nuevo rubro (perfumería, comida o indumentaria): "
            )
            rubro = rubro.lower()
            while (
                rubro != "perfumeria"
                and rubro != "perfumería"
                and rubro != "indumentaria"
                and rubro != "comida"
            ):
                print(
                    "Usted no ingreso los datos correctamente, porfavor intentelo otra vez"
                )
                separador()
                rubro = input(
                    "Ingrese el nuevo rubro del local (perfumeria, comida o indumentaria): "
                )
                rubro = rubro.lower()
            tipo = R_Loc.RubroLocal
            pos_rest = Bs_Sec_R(Rubros[:], tipo)
            pos_suma = Bs_Sec_R(Rubros[:], rubro)
            if R_Loc.RubroLocal == "perfumeria" or R_Loc.RubroLocal == "perfumería":
                Rubros_c[pos_rest] = Rubros_c[pos_rest] - 1
            elif R_Loc.RubroLocal == "indumentaria":
                Rubros_c[pos_rest] = Rubros_c[pos_rest] - 1
            else:
                Rubros_c[pos_rest] = Rubros_c[pos_rest] - 1
            if rubro == "perfumeria" or rubro == "perfumería":
                Rubros_c[pos_suma] = Rubros_c[pos_suma] + 1
                R_Loc.RubroLocal = rubro
            elif rubro == "indumentaria":
                Rubros_c[pos_suma] = Rubros_c[pos_suma] + 1
                R_Loc.RubroLocal = rubro
            else:
                Rubros_c[pos_suma] = Rubros_c[pos_suma] + 1
                R_Loc.RubroLocal = rubro
            ALL.seek(pos_reg, 0)
            R_Loc = pickle.load(ALL)
            R_Loc.RubroLocal = rubro
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
                    R_Loc = pickle.load(ALL)
                    if R_Loc.TipoUsuario.strip() == "dueños de local":
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
                        R_Loc = pickle.load(ALL)
                        if R_Loc.TipoUsuario.strip() == "dueños de local":
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
                        R_Loc.Estado = "A"  # VER SI FUNCIONA CORRECTAMENTE CON EL PROCEDIMIENTO MODIFICACION
                        if (
                            R_Loc.RubroLocal == "perfumeria"
                            or R_Loc.RubroLocal == "perfumería"
                        ):
                            re_suma = Bs_Sec_R(Rubros[:], "perfumeria")
                            Rubros_c[re_suma] = Rubros_c[re_suma] + 1
                        elif R_Loc.RubroLocal == "indumentaria":
                            re_suma = Bs_Sec_R(Rubros[:], "indumentaria")
                            Rubros_c[re_suma] = Rubros_c[re_suma] + 1
                        else:
                            re_suma = Bs_Sec_R(Rubros[:], "comida")
                            Rubros_c[re_suma] = Rubros_c[re_suma] + 1

                        Modificacion(pos)
                        separador()
                        cod_local = input(
                            "Ingrese el siguiente codigo del local que desea modificar(si no desea modificar ninguno ingrese 0): "
                        )
                else:
                    Modificacion(pos)
                    separador()
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
                        if R_Loc.RubroLocal == "perfumeria":
                            pos_rest = Bs_Sec_R(Rubros[:], "perfumeria")
                            Rubros_c[pos_rest] = Rubros_c[pos_rest] - 1
                        elif R_Loc.RubroLocal == "indumentaria":
                            pos_rest = Bs_Sec_R(Rubros[:], "indumentaria")
                            Rubros_c[pos_rest] = Rubros_c[pos_rest] - 1
                        else:
                            pos_rest = Bs_Sec_R(Rubros[:], "comida")
                            Rubros_c[pos_rest] = Rubros_c[pos_rest] - 1
                        R_Loc.Estado = "B"
                        ALL.seek(pos, 0)
                        pickle.dump(R_Loc, ALL)
                        ALL.flush()
                        os.system("cls")
                        print("El local ha sido eliminado...")
                        separador()
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
            R_Loc = pickle.load(ALL)
            T = os.path.getsize(AFL)
            if ALL.tell() < T and R_Loc.Estado == "A":
                Codigo = f"\033[1;32m{R_Loc.CodLocal}\033[0;m"
            elif ALL.tell() < T and R_Loc.Estado == "B":
                Codigo = f"\033[1;31m{R_Loc.CodLocal}\033[0;m"
            else:
                Codigo = 0
            sys.stdout.write(f" |   {Codigo}   ")
        print(" |  \n +--------+--------+--------+--------+--------+")


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
    Condicion = 0
    mostrar_menu()
    Opcion = Validacion(0, 3)
    match Opcion:
        case 1:
            Crear_Descuentos()
        case 2:
            Reporte()
        case 3:
            Ver_Nov()


def Crear_Descuentos():
    print("Crea")


def Reporte():
    print("Rep")


def Ver_Nov():
    print("Ver")


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
    print("C")


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
i_usu = 2
i_global = 1
frenar = True


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
Eleccion = Validacion(1, 3)
while Eleccion != 3:
    if Eleccion == 1:
        pedirusuario()
        match cod.strip():
            case "administrador":
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
    Eleccion = Validacion(1, 3)
