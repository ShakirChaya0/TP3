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


def separador():
    print(70 * "-")


def Exhibicion():
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
    # print("╔",12*"═","╦",14*"═","╦",30*"═","╦",30*"═","╦",12*"═","╦",6*"═","╗")   intento de hacerlo en una linea
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
    for i in range(0, i_global):
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
        item = ""
        item += "║"
        item += str(Cod_loc[i][0]).center(12)
        item += borde
        item += str(Cod_loc[i][1]).center(14)
        item += borde
        item += Datos_Locales[i][0].strip().center(30)
        item += borde
        item += Datos_Locales[i][1].strip().center(30)
        item += borde
        item += Datos_Locales[i][2].center(12)
        item += borde
        item += Datos_Locales[i][3].center(6)
        item += "║"
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


# Busqueda secuencial para registro Usuarios
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


# Sub-menus
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

    elif cod == "dueños de local":
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


# Menu del programa principal
def Menu_principal():
    print(
        """
    1. Ingresar con usuario registrado
    2. Registrarse como cliente
    3. Salir
    """
    )


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
    while len(R_Usu.NombreUsuario) > 100:
        print("Usted ingreso un mail muy largo, intente otra vez")
        R_Usu.NombreUsuario = input("Ingrese la clave del usuario: ").ljust(100, " ")

    R_Usu.ClaveUsuario = input("Ingrese la clave del usuario: ").ljust(8, " ")
    while len(R_Usu.ClaveUsuario) > 8:
        print("Usted ingreso una clave muy larga, intente otra vez")
        R_Usu.ClaveUsuario = input("Ingrese la clave del usuario: ").ljust(8, " ")

    R_Usu.TipoUsuario = "cliente"
    R_Usu.CodUsuario = i_global
    i_global = i_global + 1
    C = os.path.getsize(AFU)
    ALU.seek(C, 0)
    pickle.dump(R_Usu, ALU)
    ALU.flush()


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
    print("a")


def gestion_de_locales():
    global eleccion
    global decision

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
            while locales_cargados.lower() != "si" and locales_cargados.lower() != "no":
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
            while locales_cargados.lower() != "si" and locales_cargados.lower() != "no":
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
            while locales_cargados.lower() != "si" and locales_cargados.lower() != "no":
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


def Crear_Locales():
    verificacion = True
    global i_global

    # Busqueda dicotomica
    def Bs_Dico(x, nom):
        pri = 0
        ult = 49
        med = (pri + ult) // 2
        while x[med][0] != nom and pri <= ult:
            if x[med][0] > nom:
                ult = med - 1
            else:
                pri = med + 1
            med = (pri + ult) // 2
        if x[med][0] == nom:
            return True
        else:
            return False

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
        while verificacion == True and nombre != "0":
            verificacion = Bs_Dico(Datos_Locales[:][:], nombre)
            if verificacion == False:
                Datos_Locales[i_global][0] = nombre
            else:
                print("Usted ingreso un nombre ya existente")
                separador()
                nombre = input(
                    "Ingrese otro nombre de local (si no quiere crear locales ingrese 0): "
                )
                nombre = nombre.lower()
        verificacion = True

        if nombre != "0":
            # Cargando Ubicación:
            Ubi = input("Ingrese la ubicación para el local: ")
            while len(Ubi) > 30:
                print("Usted ingreso una ubicación muy larga... ")
                separador()
                Ubi = input("Ingrese una ubicación mas corta: ")
            Datos_Locales[i_global][1] = Ubi
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
                Datos_Locales[i_global][2] = rubro
            elif rubro == "indumentaria":
                Rubros_c[pos_suma] = Rubros_c[pos_suma] + 1
                Datos_Locales[i_global][2] = rubro
            else:
                Rubros_c[pos_suma] = Rubros_c[pos_suma] + 1
                Datos_Locales[i_global][2] = rubro

            # Cargando Estado
            Datos_Locales[i_global][3] = "A"

            # Cargando el codigo del local
            Cod_loc[i_global][0] = i_global + 1

            Cod_us = input("Ingrese el codigo de usuario: ")

            # Verificacíon y carga del codigo de usuario
            while Cod_us != "4" and Cod_us != "6":
                print("Usted ingreso un codigo de usuario erroneo, intentelo de nuevo")
                separador()
                Cod_us = input("Ingrese el codigo de usuario: ")
            Cod_us = int(Cod_us)
            Cod_loc[i_global][1] = Cod_us

            # Aumentando el contador global post carga de un local
            i_global = i_global + 1
            separador()

            Ordenamiento()

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
    # Busqueda dicotomica para el codigo
    def Bs_Dico(x, valor):
        pri = 0
        ult = i_global - 1
        med = (pri + ult) // 2
        while x[med][0] != valor and pri <= ult:
            if x[med][0] > valor:
                ult = med - 1
            else:
                pri = med + 1
            med = (pri + ult) // 2
        if x[med][0] == valor:
            return med
        else:
            return -1

    # Procedimiento para la modificación de un local:
    def Modificacion():
        verificacion = 0
        os.system("cls")
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
            while verificacion == 0:
                verificacion = Bs_Dico(Datos_Locales[:][:], nombre)
                if verificacion == -1:
                    Datos_Locales[valor][0] = nombre
                    Ordenamiento()
                else:
                    print("Usted ingreso un nombre ya existente")
                    verificacion = 0
                    separador()
                    nombre = input("Ingrese otro nombre de local: ")
                    nombre = nombre.lower()
            print("Su modificación se a realizado con exito")

        # Modificación de la ubicación:
        elif modif == "ubicacion" or modif == "ubicación":
            Ubi = input("Ingrese la nueva ubicación para el local: ")
            while len(Ubi) > 30:
                print("Usted ingreso una ubicación muy larga... ")
                separador()
                Ubi = input("Ingrese una ubicación mas corta: ")
            Datos_Locales[valor][1] = Ubi
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
            tipo = Datos_Locales[valor][2]
            pos_rest = Bs_Sec_R(Rubros[:], tipo)
            pos_suma = Bs_Sec_R(Rubros[:], rubro)
            if (
                Datos_Locales[valor][2] == "perfumeria"
                or Datos_Locales[valor][2] == "perfumería"
            ):
                Rubros_c[pos_rest] = Rubros_c[pos_rest] - 1
            elif Datos_Locales[valor][2] == "indumentaria":
                Rubros_c[pos_rest] = Rubros_c[pos_rest] - 1
            else:
                Rubros_c[pos_rest] = Rubros_c[pos_rest] - 1
            if rubro == "perfumeria" or rubro == "perfumería":
                Rubros_c[pos_suma] = Rubros_c[pos_suma] + 1
                Datos_Locales[valor][2] = rubro
            elif rubro == "indumentaria":
                Rubros_c[pos_suma] = Rubros_c[pos_suma] + 1
                Datos_Locales[valor][2] = rubro
            else:
                Rubros_c[pos_suma] = Rubros_c[pos_suma] + 1
                Datos_Locales[valor][2] = rubro
            print("Su modificación se a realizado con exito")

        # Modificación del código de usuario
        elif modif == "codigo de usuario":
            Cod_us = input("Ingrese el nuevo codigo de usuario: ")
            while Cod_us != "4" and Cod_us != "6":
                print("Usted ingreso un codigo de usuario erroneo, intentelo de nuevo")
                separador()
                Cod_us = input("Ingrese el nuevo codigo de usuario: ")
            Cod_us = int(Cod_us)
            Cod_loc[valor][1] = Cod_us
            print("Su modificación se a realizado con exito")
        else:
            print("No se realizó ninguna modificación")

    cod_local = input(
        "Ingrese el codigo del local que desea modificar(si no desea modificar ninguno ingrese 0): "
    )
    while cod_local != "0":
        if cod_local.isdigit():
            cod_local = int(cod_local)
            valor = Bs_Sec(Cod_loc[:][:], cod_local)
            if valor == -1:
                print("Usted ingreso un valor no valido, intentelo de nuevo")
                separador()
                cod_local = input(
                    "Ingrese el codigo del local que desea modificar(si no desea modificar ninguno ingrese 0): "
                )
            else:
                print("Local encontrado!!!")
                if Datos_Locales[valor][3] == "B":
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
                        pos = Bs_Sec(Cod_loc[:][:], cod_local)
                        Datos_Locales[pos][3] = "A"
                        if (
                            Datos_Locales[pos][2] == "perfumeria"
                            or Datos_Locales[pos][2] == "perfumería"
                        ):
                            re_suma = Bs_Sec_R(Rubros[:], "perfumeria")
                            Rubros_c[re_suma] = Rubros_c[re_suma] + 1
                        elif Datos_Locales[pos][2] == "indumentaria":
                            re_suma = Bs_Sec_R(Rubros[:], "indumentaria")
                            Rubros_c[re_suma] = Rubros_c[re_suma] + 1
                        else:
                            re_suma = Bs_Sec_R(Rubros[:], "comida")
                            Rubros_c[re_suma] = Rubros_c[re_suma] + 1

                        Modificacion()
                        separador()
                        cod_local = input(
                            "Ingrese el siguiente codigo del local que desea modificar(si no desea modificar ninguno ingrese 0): "
                        )
                else:
                    Modificacion()
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
            pos = Bs_Sec(Cod_loc[:][:], eliminar)
            if pos == -1:
                print("Usted ingreso un valor no valido, intentelo de nuevo")
                separador()
                eliminar = input(
                    "Ingrese el codigo del local que desea eliminar(si no desea modificar ninguno ingrese 0): "
                )
            else:
                print("Local encontrado!!!")
                if Datos_Locales[pos][3] == "B":
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
                        Datos_Locales[pos][3] = "B"
                        if Datos_Locales[pos][2] == "perfumeria":
                            pos_rest = Bs_Sec_R(Rubros[:], "perfumeria")
                            Rubros_c[pos_rest] = Rubros_c[pos_rest] - 1
                        elif Datos_Locales[pos][2] == "indumentaria":
                            pos_rest = Bs_Sec_R(Rubros[:], "indumentaria")
                            Rubros_c[pos_rest] = Rubros_c[pos_rest] - 1
                        else:
                            pos_rest = Bs_Sec_R(Rubros[:], "comida")
                            Rubros_c[pos_rest] = Rubros_c[pos_rest] - 1
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
    C = 0
    print("                 Mapa de Locales")
    print("", "+--------+--------+--------+--------+--------+")
    for i in range(0, 10):
        for j in range(0, 5):
            if Datos_Locales[C + j][0] != " ":
                Codigo = Cod_loc[C + j][0]
            else:
                Codigo = 0
            sys.stdout.write(f" |   {Codigo}   ")
        print(" |  \n +--------+--------+--------+--------+--------+")
        C = C + 5


# Declaración de variables...
eleccion = -1
bandera = 0
i_global = 2
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


####### PROGRAMA PRINCIPAL ########

Menu_principal()
elec = input("Seleccione la opción que desee: ")
while elec != 3 and bandera == 0:
    try:
        elec = int(elec)
        if elec == 1:
            pedirusuario()
            match cod.strip():
                case "administrador":
                    mostrar_menu()
                    Admin()
                case "dueños de local":
                    mostrar_menu()
                    DueñoDelocales()
                case "cliente":
                    mostrar_menu()
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
