"""
imatlab.py

Matemática Discreta - IMAT
ICAI, Universidad Pontificia Comillas

Grupo: GP04B
Integrantes:
    - Gonzalo Miguel Torrente Belío
    - Juan Rincón Pérez

Descripción:
Sistema interactivo IMAT-LAB de resolución de ecuaciones en aritmética modular.

Interfaz de acceso interactivo o por lotes a la librería modular.py. Si este script se ejecuta sin parámetros,
lanzaría la interfaz de usuario para el modo interactivo.
"""

from typing import TextIO
import modular
import sys


dicc_operations = {                                                                                                     
                    "primo": modular.primo, 
                    "primos": modular.primos, 
                    "factorizar": modular.factorizar_aux,
                    "mcd": modular.mcd_imatlab,
                    "bezout": modular.bezout,
                    "coprimos": modular._coprimos,
                    "pow": modular.pow,
                    "inv": modular.inv,
                    "euler": modular.euler,
                    "legendre": modular.legendre,
                    "resolverSistema": modular.resolverSistema,
                    "raiz": modular.raiz,
                    "ecCuadratica": modular.ecCuadratica
                }


def run_commands(fin:TextIO,fout:TextIO):
    """ Recibe un manejador fin de un fichero de texto ya abierto para lectura y otro de un fichero de salida
    ya abierto para escritura y ejecuta línea por línea los comandos proporcionados por fin, escribiendo los resultados en fout.
    Si fin y fout no corresponden con la entrada y salida estándar, esta función ejecuta el modo de procesamiento
    por lotes de IMAT-LAB para la entrada fin, guardando el resultado en el fichero fout.

    Args:
        fin (TextIO): Fichero de entrada. Manejador de un fichero de texto ya abierto para lectura.
        fout (TextIO): Fichero de salida. Manejador de un fichero de texto ya abierto para escritura.
    
    Returns: None
    
    Raises: None
    
    Examples:
        run_commands(sys.stdin,sys.stdout) lanza el modo interactivo y ejecuta línea por línea los comandos que
            el usuario lanza desde la entrada estándar.
    """
    # condición de parada 
    # leer linea
    #separamos la función de operación de los argumentos
    cond = True
    is_interactivo = fin is sys.stdin and fout is sys.stdout # Comprobamos si estamos en modo interactivo para mostrar errores personalizados
    while cond:
        try:
            linea = fin.readline()
            linea = linea.strip()

            if linea == "":
                cond = False

            else:
                a = linea.find("(")

                if a == -1 or not linea.endswith(")"):
                    raise ValueError("Los comandos deben introducir los argumentos entre paréntesis")

                else:
                    operacion = linea[:a].strip()
                    argumentos = linea[a + 1:-1]

                    if operacion not in dicc_operations:
                        fout.write("NOP\n")

                    else:
                        llamada = dicc_operations.get(operacion)

                        if argumentos.strip() == "":
                            lista_arg = []

                        else:
                            lista_arg = argumentos.split(",")

                        # Convertimos los argumentos a int o List[int]
                        i = 0

                        for argumento in lista_arg:
                            argumento = argumento.strip()


                            if argumento.startswith("[") and argumento.endswith("]"):
                                contenido = argumento[1:-1]

                                if contenido.strip() == "":
                                    raise ValueError("No se han introducido argumentos")

                                argumentos_lista = contenido.split(";")
                                nueva_lista = []

                                for subargumento in argumentos_lista:
                                    nueva_lista.append(int(subargumento.strip()))

                                lista_arg[i] = nueva_lista

                            else:
                                lista_arg[i] = int(argumento)

                            i += 1

                        resultado = llamada(*lista_arg)
                        fout.write(str(resultado) + "\n")
                        
        except (modular.IncompatibleEquationError, ZeroDivisionError) as error:
            if not is_interactivo:
                fout.write(f"NE\n")
            else:
                fout.write(f"{error}\n")

        except (ValueError, TypeError, IndexError) as error:
            if not is_interactivo:
                fout.write(f"NOP\n")
            else:
                fout.write(f"{error}\n")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        run_commands(sys.stdin, sys.stdout)

    elif len(sys.argv) == 3:
        with open(sys.argv[1], "r") as fin:
            with open(sys.argv[2], "w") as fout:
                run_commands(fin, fout)

    else:
        print("NOP")