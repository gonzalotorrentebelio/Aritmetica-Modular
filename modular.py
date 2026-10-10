"""
modular.py

Matemática Discreta - IMAT
ICAI, Universidad Pontificia Comillas

Grupo: GPxxx
Integrantes:
    - Juan Rincón Pérez
    - XX

Descripción:
Librería para la realización de cálculos y resolución de problemas de aritmética modular.
"""

from typing import Tuple, List, Dict
import math

class IncompatibleEquationError(Exception):
    pass

def primo(n:int)->str:
    """
    Función auxiliar de es_primo() para transformar la salida a la esperada en fout
    Args:
        n (int): Entero
    
    Returns:
        "Sí" si el_primo() es True.
        "No" si el_primo() es False.
    """

    if es_primo(n):
        return "Sí"
    
    return "No"


def es_primo(n:int)->bool:
    """ Reciba un entero n y devuelva verdadero si es un número primo y falso en caso contrario

    Args:
        n (int): Entero
    
    Returns:
        true si el entero es un número primo.
        false en caso contrario.

    Raises: None
    
    Examples:
        es_primo(5)=True
        es_primo(4)=False
    """
    if n < 2:
        return False
    
    if n < 4:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    cota_sup = math.sqrt(n)
    divisor = 5
    while divisor <= cota_sup:
        if n % divisor == 0 or n % (divisor + 2) == 0:  
            return False
        divisor += 6   #Cada 6, 4 son no primos al 100%. Los divisores de 2, los de 3

    return True


def primos(a,b)->str:
    
    prime_list = lista_primos(a,b)
    if prime_list == []:
        return "NE"
    
    return str(prime_list)[1:-1]


def lista_primos(a,b)-> List[int]:
    """ Recibe dos enteros a y b y devuelva la lista de números primos en el intervalo [a, b)

    Args:
        a (int): Elemento inicial del intervalo (incluido)
        b (int): Elemento final del intervalo (no incluido)
    
    Returns:
        List[int]: lista ordenada de primos mayores o iguales que a y menores que b.

    Raises: None
    
    Examples:
        lista_primos(1,11)=[2,3,5,7]
    """
    
    if a < 2:
        a = 2

    if a >= b:
        return []

    tabla = [True] * b
    tabla[0] = False
    tabla[1] = False

    p = 2
    while p * p < b:
        if tabla[p]:
            for m in range(p*p, b, p):
                tabla[m] = False
        p += 1

    lista_primos = []
    for i in range(a, b):
        if tabla[i]:
            lista_primos.append(i)
    
    return lista_primos

def factorizar_aux(n:int)->str:
    dic_fact = factorizar(n)
    if dic_fact == {}:
        return f"{n}"
    
    else:
        return str(dic_fact)[1:-1]


def factorizar(n:int)->Dict[int,int]:
    """ Recibe  un entero n y devuelve un diccionario cuyas claves son los primos que dividen a n y sus valores los
    correspondientes exponentes en la descomposición en producto de factores primos de n.
    Args:
        n (int): Entero que se desea factorizar.
    
    Returns:
        Dict[int,int]: Diccionario en el que las claves son primos positivos p_i que dividen a n y, para cada p_i,
            su valor asociado es el máximo exponente e_i tal que p_i^(e_i) divide a n. Si n=0, devuelve un diccionario vacío.

    Raises: None

    Examples:
        factorizar(12)={2: 2, 3: 1}
        factorizar(0)={}
    """
    
    if n == 0 or n == 1 or n == -1:
        return {}
    
    dic = {} 
    n = abs(n)

    for p in range(2,4):
        count = 0
        while n % p == 0:
            n = n // p
            count += 1
        
        if count > 0:
            dic[p] = count

    m = 5
    while m * m <= n:  # es lo mismo que decir m <= cota_sup donde cota_sup = np.sqrt(n)
        for d in (m, m + 2):
            count = 0
            while n % d == 0:
                n = n // d
                count += 1
            
            if count > 0:
                dic[d] = count

        m += 6

    if n > 1:
        dic[n] = 1
    
    return dic

def mcd_imatlab(*args):
    if len(args) == 2:
        return mcd(args[0], args[1])
    return mcd_n(list(args))

def mcd(a:int,b:int = 0)->int:
    """ Calcula el máximo común divisor de dos enteros a y b.
    Args:
        a (int): Primer entero.
        b (int): Segundo entero.
    
    Returns:
        int: devuelve el máximo común divisor de a y b

    Raises: None

    Examples:
        mcd(10,15)=5
    """
    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return a

def bezout(n: int, m: int) -> Tuple[int, int, int]:
    """Calcula el máximo común divisor d de dos enteros n y m junto con
    dos enteros x e y tales que d = nx + my.

    Args:
        n (int): Primer entero.
        m (int): Segundo entero.
    
    Returns: (d, x, y)
        d (int): Máximo común divisor.
        x (int): Coeficiente de n.
        y (int): Coeficiente de m.

    Raises: None

    Examples:
        bezout(6, 10) = (2, 2, -1)
    """

    coord_n = [1, 0]
    coord_m = [0, 1]

    while m != 0:
        k = n // m
        n, m, coord_n, coord_m = m, n % m, coord_m, [coord_n[0] - k * coord_m[0], coord_n[1] - k * coord_m[1]] # Algoritmo de euclides, pongo el grande como primero y calculo coords, las de m cambian a las de n y las nuevas de m se calculan como coord_n - (cuantos m quito) * coord_n

    if n < 0:
        n, coord_n = -n, [-coord_n[0], -coord_n[1]] # Si es negativo se pasa a positivo 

    return n, coord_n[0], coord_n[1]


def mcd_n(nlist:List[int])-> int:
    """ Dados una lista de enteros, devuelve el máximo divisor común a todos ellos.
    Args:
        nList (List[int]): Lista de enteros.        
    
    Returns:
        int: devuelve el máximo entero que divide a todos los enteros de la lista.

    Raises: None

    Examples:
        mcd([4,10,14])=2
    """
    # Opcional
    resultado = nlist[0]

    for i in nlist[1:]:
        resultado = mcd(resultado, i)

        if resultado == 1:
            return 1 # mcd(x, y, z, ..., 1) = 1 porque el uno no tiene mas divisores positivos que el mismo

    return resultado


def bezout_n(nlist:List[int])->Tuple[int,List[int]]:
    # Opcional
    """ Dada una lista de enteros [a_1,...,a_n], devuelve el máximo divisor común d a todos ellos y una
    lista de coeficientes [x_1,...,x_n] tal que
        d=a_1*x_1+...a_n*x_n

    Args:
        nList (List[int]): Lista de enteros.        
    
    Returns: (d,X)
        d (int): Máximo entero que divide a todos los enteros de la lista.
        X (List[int]): Lista de coeficientes [x_1,...,x_n].

    Raises: None

    Examples
        bezout_n([4,10,14])=(2,[-2,1,0])
    """
    # Igual que en el mcd_n, vamos haciendo bezout de dos en dos y guardamos los coeficientes de forma que a1x1 + a2x2 + a3x3 + ... = mcd(x1, x2, x3,...) podemos resolver a1x1 + a2x2 = mcd(x1,x2) = d1, entonces queda A1d1 + a3x3 = mcd(x1,x2,x3) ya que mcd (d1, x3,...) es igual, luego solo queda ver que coord_finales = a1 * A1, a2*A1. Hay que ir multiplicando por los nuevos que se consiguen
    resultado_mcd, coord_0, coord_1 = bezout(nlist[0], nlist[1])
    coeficientes = [coord_0, coord_1]

    for i in nlist[2:]:
        resultado_mcd, coord_anteriores, coord_i = bezout(resultado_mcd, i)

        for j in range(len(coeficientes)):
            coeficientes[j] *= coord_anteriores

        coeficientes.append(coord_i)

    return resultado_mcd, coeficientes

def coprimos(n:int,m:int)->bool:
    """ Determina si dos enteros son coprimos.
    Args:
        a (int): Primer entero.
        b (int): Segundo entero.
    
    Returns:
        bool: Verdadero si son coprimos y falso si no.

    Raises: None

    Examples:
        coprimos(14,20)=False
        coprimos(14,15)=True
    """
    return mcd(n, m) == 1

def _coprimos(n:int, m:int) -> str:
    if coprimos(n, m):
        return "Sí"
    return "No"


def pow(base:int, exp:int, p:int) -> str:
    '''
    Devuelve el resultado de potencia_mod_p() en formato string.
    
    '''
    return str(potencia_mod_p(base, exp, p))

def potencia_mod_p(base:int, exp:int, p:int) -> int:
    """ Calcula potencias módulo p.

    Args:
        base (int): Base de la potencia.
        exp (int): Exponente al que se eleva la base.
        p (int): Módulo.
    
    Returns:
        int: Resto de dividir base^exp módulo p.

    Raises:
        ZeroDivisionError: Si el módulo es 0 o si la base y el exponente
        son ambos 0 al mismo tiempo.

    Examples:
        potencia_mod_p(2,3,7)=1
    """
    if p == 0:
        raise ZeroDivisionError()
    
    if base == 0 and exp == 0:
        raise ZeroDivisionError()
    
    if exp < 0:
        phi_p = euler(p)
        exp = exp % phi_p

    base = base % p # resuelve bases negatvas y las que son mayores q 'p'
    resultado = 1% p # te ahorras el caso especial p == 1 y exp == 0
    while exp > 0:  # aplicamos la propiedad (a * b) mod p = ((a mod p) * (b mod p)) mod p 
        if exp % 2 == 1: # lo recorre en modo binario con ayuda de exp = exp//2
            resultado = (resultado * base) % p
        
        base = (base* base) % p  # devuelve la siguiente potencia al cuadrado
        exp = exp //2  # desplaza un bit hacia la derecha
    return resultado

def inv(n : int,p: int) -> int:
    return inversa_mod_p(n,p)


def inversa_mod_p(n:int,p:int)->int:
    """ Calcula la inversa de un número n módulo p.

    Args:
        n (int): Número que se desea invertir
        p (int): Módulo.
    
    Returns:
        int: Entero x entre 0 y p-1 tal que n*x es congruente con 1 módulo p.

    Raises:
        ZeroDivisionError: Si el módulo es 0 o si n no es invertible módulo p.
    
    Examples:
        inversa_mod_p(2,7)=4
    """
    if p == 0:
        raise ZeroDivisionError("El módulo no puede ser 0")

    # Euclides extendido arrastrando solo el coeficiente de n, que es el único que
    # necesitamos: de la identidad de Bezout d = n*x + p*y, la inversa es x.
    r_ant, r_act = p, n % p     # restos sucesivos del algoritmo de Euclides
    x_ant, x_act = 0, 1         # coeficiente de n en cada uno de esos restos

    while r_act != 0:
        q = r_ant // r_act
        r_ant, r_act = r_act, r_ant - q * r_act
        x_ant, x_act = x_act, x_ant - q * x_act

    if r_ant != 1:              # el mcd no es 1, luego n no es invertible modulo p
        raise ZeroDivisionError("n no es invertible módulo p")

    return x_ant % p            # hacemos el módulo porque x_ant no tiene por qué estar entre 0 y p-1


def euler(n:int)->int:
    """ Calcula la función phi de Euler de un entero positivo n, es decir, cuenta cúantos enteros positivos
    menores que n son coprimos con n.

    Args:
        n (int): Número entero positivo.
    
    Returns:
        int: Función phi de Euler de n.

    Raises: None

    Examples:
        euler(7)=6
        euler(15)=8
    """
    # phi es multiplicativa: phi(p1^e1 * ... * pk^ek) = phi(p1^e1) * ... * phi(pk^ek),
    # y para una potencia de primo phi(p^e) = p^(e-1) * (p-1)
    pass
    if n < 1:
        raise ValueError("n debe ser un entero positivo")
    
    resultado = 1
    for p, e in factorizar(n).items():
        resultado *= (p - 1) * p ** (e-1)

    return resultado


def legendre(n:int,p:int)->int:
    """ Dado un entero n y un número primo p, calcula el símbolo de Legendre de n módulo p.

    Args:
        n (int): Número entero.
        p (int): Número primo.
    
    Returns:
        int: Símbolo de Legendre de Euler de n módulo p:
            0 si es múltiplo de p
            1 si es un cuadrado perfecto (distinto de 0), módulo p
            -1 en caso contrario.

    Raises:
        ZeroDivisionError: Si el módulo p es 0.

    Examples:
        legendre(2,5)=-1
        legendre(2,7)=1
        legendre(10,5)=0
    """
    if p == 0:
        raise ZeroDivisionError
    
    n %= p

    if n == 0:
        return 0

    resultado = potencia_mod_p(n, (p - 1) // 2, p) # Criterio de Euler

    if resultado == p - 1:
        return -1

    return 1


def resolver_sistema_congruencias(alist:List[int],blist:List[int],plist:List[int])->Tuple[int,int]:
    """ Dadas tres listas de números enteros [a_1,...,a_n], [b_1,...,b_n] y [p_1,...,p_n], resuelve el sistema de congruencias
    
    a_i * x = b_i (mod p_i)   i=1,...,n
    
    devolviendo un entero r y un módulo m tales que las soluciones del sistema corresponden a todos los enteros
    x congruentes con r módulo m.

    Args:
        alist (List[int]): Lista de coeficientes de la variable x, [a_1,...,a_n].
        blist (List[int]): Lista de términos independientes [b_1,...,b_n].
        plist (List[int]): Lista de módulos [p_1,...,p_n]
    
    Returns: (r,m)
        r (int): Entero entre 0 y m-1.
        m (int): Entero positivo, módulo de la solución.

    Raises:
        IncompatibleEquationError: Si no es posible resolver el sistema.

    Examples:
        resolver_sistema_congruencias([2],[3],[5]])=(4,5)
        resolver_sistema_congruencias([2],[4],[6])=(2,3)
        resolver_sistema_congruencias([1,4],[1,7],[3,11])=(10,33)
    """
    # Teorema Chino del resto incremental. En vez de contruir las soluciones con la fórmula se construyen con la definición de congruencia
    # Si tenemos X ≅ A (mod p) -> X - A = p * k, entonces sacaremos que X = A + p * k como primera solución. X ≅ B (mod q) -> X - B = q * t,
    # pero ya tenemos una expresión para X así que A + p * k - B = q * t, que despejando me queda p * k = B - A + q * t -> p * k ≅ B - A (mod q)
    # y ahora k es nuestra incógnita (x particular) que sumaremos a la x general multiplicada por p ya que x = A + p*k
    # Se puede ver como que la solucion de la primera es una lista de números x = A + p * k, con k variando. Con la segunda ecuación solo
    # cogemos los de las listas que coincidan. Vamos haciendo esto con cada lista particularizando, y nos quedará un patrón de números con
    # saltos entre ellos, que es el módulo final
    x = 0
    m = 1

    for a, b, p in zip(alist, blist, plist):
        div = mcd(a, p)

        if b % div != 0:
            raise IncompatibleEquationError

        a, b, p = a // div, b // div, p // div
        r = (inversa_mod_p(a, p) * b) % p

        div = mcd(m, p)

        if (r - x) % div != 0: # Como r - x sería nuestra b inicial no hay sol si b % div != 0
            raise IncompatibleEquationError

        m_red = m // div
        p_red = p // div
        dif = (r - x) // div

        k = (dif * inversa_mod_p(m_red, p_red)) % p_red

        x += m * k
        m *= p_red
        x %= m

    return x, m

def resolverSistema(*listas:List[int]) -> str:
    alist = []
    blist = []
    plist = []
    for a, b, p in listas:
        alist.append(a)
        blist.append(b)
        plist.append(p)

    x, m = resolver_sistema_congruencias(alist, blist, plist)
    return str(F"{x} (mod {m})")

def raiz_mod_p(n:int,p:int)->int:
    """ Encuentra, si existe, una raíz cuadrada para un entero n módulo un número primo p.

    Args:
        n (int): Entero del que se desea hallar la raíz.
        p (int): Módulo. Se asume que es un número primo.
    
    Returns:
        int: Entero x entre 0 y p-1 tal que x^2 = n (mod p).

    Raises:
        IncompatibleEquationError: Si no es posible hallar dicha raíz.

    Examples:
        raiz_mod_p(2,7)=3
    """
    #Opcional
    n %= p

    if p == 2 or n == 0:
        return n

    # p ≡ 3 (mod 4)
    if p % 4 == 3:
        x = potencia_mod_p(n, (p + 1) // 4, p)

        if x * x % p != n:
            raise IncompatibleEquationError

        return x

    # p ≡ 5 (mod 8)
    if p % 8 == 5:
        x = potencia_mod_p(n, (p + 3) // 8, p)

        if x * x % p != n:
            x = x * potencia_mod_p(2, (p - 1) // 4, p) % p

        if x * x % p != n:
            raise IncompatibleEquationError

        return x

    # p ≡ 1 (mod 8): primero comprobamos que exista raíz
    if potencia_mod_p(n, (p - 1) // 2, p) != 1:
        raise IncompatibleEquationError

    # p - 1 = q * 2^s, q impar
    q = p - 1
    s = 0

    while q % 2 == 0:
        q //= 2
        s += 1

    # Buscar un no-residuo cuadrático
    z = 2
    while potencia_mod_p(z, (p - 1) // 2, p) != p - 1:
        z += 1

    # Tonelli-Shanks
    m = s
    c = potencia_mod_p(z, q, p)
    x = potencia_mod_p(n, (q + 1) // 2, p)
    t = potencia_mod_p(n, q, p)

    while t != 1:
        i = 1
        aux = t * t % p

        while aux != 1:
            aux = aux * aux % p
            i += 1

        b = potencia_mod_p(c, 1 << (m - i - 1), p)

        x = x * b % p
        b = b * b % p
        t = t * b % p
        c = b
        m = i

    return x

def raiz(n: int, p: int) -> str:
    """
    Formatea la salida según el criterio especificado
    """
    x1 = raiz_mod_p(n, p)
    x2 = (-x1) % p

    if x1 == x2:
        return str(x1)

    if x1 > x2:
        x1, x2 = x2, x1

    return f"{x1}, {x2}"


def ecuacion_cuadratica(a:int,b:int,c:int,p:int)->Tuple[int,int]:
    """ Halla, si es posible, las dos posibles soluciones de la ecuación cuadrática ax^2+bx+c=0 (mod p).
    Devuelve una tupla con las dos raíces (distintas o una misma raíz repetida en caso de ser doble).

    Args:
        a (int): Coeficiente de x^2.
        b (int): Coeficiente de x.
        c (int): Término independiente.
        p (int): Módulo. Se asume que es un número primo.
    
    Returns: (x1,x2)
        x1 (int): Primera solución. Entero entre 0 y p-1.
        x2 (int): Segunda solución. Entero entre 0 y p-1.

    Raises:
        IncompatibleEquationError: Si no es posible resolver la ecuación.

    Examples:
        ecuacion_cuadratica(4,1,3,11)
        ecuacion_cuadratica(4,1,5,11)=(3, 5)
        ecuacion_cuadratica(1,2,1,11)=(10,10)
    """
    # Opcional
    # Despejar como x = (-b +- raiz(b^2 - 4ac)) / 2a, /2a será (2a)-1 (mod p)
    # La raíz puede ser negativa porque -1 (p) = p - 1 (p)
    discriminante = (b ** 2 - 4 * a * c) % p
    raiz = raiz_mod_p(discriminante, p)
    inversa_2a = inversa_mod_p(2 * a, p)

    # X2 > X1
    x1 = (-b - raiz) * inversa_2a
    x2 = (-b + raiz) * inversa_2a

    return x2 % p, x1 % p

def ecCuadratica(a: int, b: int, c: int, p: int) -> str:
    """
        Formatea la salida según el criterio especificado
    """
    x1, x2 = ecuacion_cuadratica(a, b, c, p)

    if x1 == x2:
        return str(x1)

    if x1 > x2:
        x1, x2 = x2, x1

    return f"{x1}, {x2}"