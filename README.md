# IMAT-LAB · Aritmética modular

Práctica 1 de **Matemática Discreta** (Grado en Ingeniería Matemática e Inteligencia Artificial, ICAI – Universidad Pontificia Comillas, curso 2026-2027).

**Grupo GP04B**

- Gonzalo Miguel Torrente Belío
- Juan Rincón Pérez

El proyecto consta de una librería de aritmética modular escrita en Python puro (`modular.py`) y de un intérprete de comandos, **IMAT-LAB** (`imatlab.py`), que permite usarla de forma interactiva o procesando ficheros de comandos por lotes.

---

## Requisitos

- Python 3.8 o superior (probado con Python 3.13).
- La librería y el intérprete solo usan la biblioteca estándar (`math`, `sys`, `typing`).
- Para los tests unitarios hace falta `pytest`.

```bash
pip install -r requirements.txt
```

---

## Estructura del proyecto

```
Artimetica-Modular/
├── modular.py               # Librería de aritmética modular
├── imatlab.py               # Intérprete IMAT-LAB (modo interactivo y por lotes)
├── imatlab_benchmark.py     # Medición de tiempos (timeit) y perfilado (cProfile)
├── ejemplosComandos.txt     # Comandos de ejemplo
├── ejemplosSalida.txt       # Salida esperada para ejemplosComandos.txt
├── test_imatlab.py          # Tests generales de entrada/salida + try_command()
├── test_P1_es_primo.py      # Tests unitarios por ejercicio (P1 … P14)
├── test_P2_lista_primos.py
├── test_P3_factorizar.py
├── test_P4_P5_mcd.py
├── test_P6_coprimos.py
├── test_P7_potencia.py
├── test_P8_inversa.py
├── test_P9_euler.py
├── test_P10_legendre.py
├── test_P11_P12_sistema.py
├── test_P13_P14_raiz.py
├── tests/                   # Ficheros de benchmark
│   ├── primosTest.txt
│   ├── factorTest.txt
│   ├── mcdTest.txt
│   ├── potenciaTest.txt
│   ├── invTest.txt
│   ├── eulerTest.txt
│   ├── sistemaTest.txt
│   └── cuadraticaTest.txt
├── requirements.txt
└── README.md
```

---

## Uso

### Modo interactivo

```bash
python imatlab.py
```

Se escribe un comando por línea y el resultado aparece inmediatamente. Una línea vacía termina la sesión.

```
primo(7)
Sí
factorizar(120)
2: 3, 3: 1, 5: 1
inv(3,9)
 3 no es invertible módulo 9, tienen factores comunes
```

En este modo, en lugar de los códigos `NE` / `NOP`, se muestra un **mensaje de error descriptivo** (por ejemplo, «No existe raíz de 3 módulo 7»).

### Modo por lotes

```bash
python imatlab.py fichero_entrada.txt fichero_salida.txt
```

Ejecuta los comandos del fichero de entrada línea a línea y escribe un resultado por línea en el fichero de salida. El procesamiento se detiene en la primera línea vacía. Por ejemplo:

```bash
python imatlab.py ejemplosComandos.txt salida.txt
```

genera un fichero idéntico a `ejemplosSalida.txt`.

Cualquier otro número de argumentos imprime `NOP`.

### Desde Python

```python
import sys
import imatlab

with open("ejemplosComandos.txt") as fin, open("salida.txt", "w", encoding="utf-8") as fout:
    imatlab.run_commands(fin, fout)        # modo por lotes

imatlab.run_commands(sys.stdin, sys.stdout)  # modo interactivo
```

`run_commands` decide el modo comprobando si los manejadores recibidos son exactamente `sys.stdin` y `sys.stdout`.

---

## Comandos de IMAT-LAB

| Comando | Descripción | Ejemplo | Salida |
|---|---|---|---|
| `primo(n)` | ¿Es `n` primo? | `primo(7)` | `Sí` |
| `primos(a, b)` | Primos en el intervalo `[a, b)` | `primos(5,20)` | `5, 7, 11, 13, 17, 19` |
| `factorizar(n)` | Factorización en primos (`n` si `n ∈ {-1, 0, 1}`) | `factorizar(120)` | `2: 3, 3: 1, 5: 1` |
| `mcd(a1, …, an)` | Máximo común divisor de dos o más enteros | `mcd(12,18,30)` | `6` |
| `bezout(a, b)` | Identidad de Bézout `d = a·x + b·y` *(comando adicional)* | `bezout(6,10)` | `(2, 2, -1)` |
| `coprimos(a, b)` | ¿Son coprimos? | `coprimos(6,9)` | `No` |
| `pow(base, exp, p)` | `base^exp mod p` (admite exponentes negativos) | `pow(-3,-8,7)` | `4` |
| `inv(n, p)` | Inverso de `n` módulo `p` | `inv(3,7)` | `5` |
| `euler(n)` | Función φ de Euler | `euler(10)` | `4` |
| `legendre(n, p)` | Símbolo de Legendre (n/p) | `legendre(10,3)` | `1` |
| `resolverSistema([a;b;p], …)` | Sistema de congruencias `a·x ≡ b (mod p)` | `resolverSistema([1;1;3],[4;7;11])` | `10 (mod 33)` |
| `raiz(n, p)` | Raíces cuadradas de `n` módulo `p` primo | `raiz(-1,5)` | `2, 3` |
| `ecCuadratica(a, b, c, p)` | Soluciones de `ax² + bx + c ≡ 0 (mod p)` | `ecCuadratica(4,1,5,11)` | `3, 5` |

Los nombres de comando distinguen mayúsculas y minúsculas (`Legendre(10,3)` → `NOP`).

### Códigos de error (modo por lotes)

| Código | Significado |
|---|---|
| `NE` | El problema no tiene solución (p. ej. `inv(3,9)`, sistema incompatible, `n` sin raíz cuadrada, lista de primos vacía). |
| `NOP` | Llamada incorrecta: comando inexistente, sintaxis mal formada, número o tipo de argumentos erróneo. |

Ninguna entrada, por mal formada que esté, provoca la terminación del programa: todas las excepciones se capturan en `run_commands`.

---

## La librería `modular.py`

Funciones con la interfaz exigida por el enunciado:

| Ejercicio | Función | Algoritmo |
|---|---|---|
| 1 | `es_primo(n) -> bool` | División por tentativa con la rueda `6k ± 1` hasta `√n` |
| 2 | `lista_primos(a, b) -> List[int]` | Criba de Eratóstenes sobre `[0, b)`, tachando desde `p²` |
| 3 | `factorizar(n) -> Dict[int, int]` | División por 2, 3 y después por candidatos `6k ± 1` hasta `√n` |
| 4 | `mcd(a, b) -> int` | Algoritmo de Euclides |
| 4 | `bezout(a, b) -> Tuple[int, int, int]` | Algoritmo de Euclides extendido |
| 5 *(opc.)* | `mcd_n(nlist) -> int` | Euclides iterado, con corte anticipado al llegar a 1 |
| 5 *(opc.)* | `bezout_n(nlist) -> Tuple[int, List[int]]` | Bézout iterado reescalando los coeficientes previos |
| 6 | `coprimos(a, b) -> bool` | `mcd(a, b) == 1` |
| 7 | `potencia_mod_p(base, exp, p) -> int` | Exponenciación binaria (*square-and-multiply*); exponente negativo vía inversa |
| 8 | `inversa_mod_p(n, p) -> int` | Euclides extendido arrastrando solo el coeficiente de `n` |
| 9 | `euler(n) -> int` | Multiplicatividad: φ(pᵉ) = pᵉ⁻¹(p − 1) sobre la factorización |
| 10 | `legendre(n, p) -> int` | Criterio de Euler: n^((p−1)/2) mod p |
| 11-12 | `resolver_sistema_congruencias(alist, blist, plist) -> Tuple[int, int]` | Teorema chino del resto incremental; admite módulos **no coprimos** (opc. 12) y coeficientes `aᵢ ≠ 1` |
| 13 *(opc.)* | `raiz_mod_p(n, p) -> int` | Casos directos para p ≡ 3 (mod 4) y p ≡ 5 (mod 8) (Atkin); Tonelli-Shanks para p ≡ 1 (mod 8) |
| 14 *(opc.)* | `ecuacion_cuadratica(a, b, c, p) -> Tuple[int, int]` | Fórmula cuadrática modular: x = (−b ± √Δ)·(2a)⁻¹ mod p |

Además, `modular.py` contiene funciones envoltorio (`primo`, `primos`, `factorizar_aux`, `mcd_imatlab`, `_coprimos`, `pow`, `inv`, `resolverSistema`, `raiz`, `ecCuadratica`) que adaptan la salida de cada función al formato de texto que debe imprimir IMAT-LAB.

### Excepciones

- `IncompatibleEquationError`: ecuación o sistema sin solución, o número sin raíz cuadrada modular.
- `ZeroDivisionError`: módulo 0, `0^0` o elemento no invertible.
- `ValueError`: argumento fuera de dominio (p. ej. `euler(n)` con `n < 1`).

IMAT-LAB traduce las dos primeras a `NE` y los errores de formato (`ValueError`, `TypeError`, `IndexError`) a `NOP`.

---

## Tests

Los tests unitarios (pytest) están en la raíz del proyecto, un fichero por ejercicio. Cada fichero comprueba tanto la función de `modular.py` como el comando correspondiente de IMAT-LAB, usando el auxiliar `try_command` de `test_imatlab.py`.

```bash
pytest            # todos los tests
pytest test_P8_inversa.py   # un ejercicio concreto
```

Estado actual: **195 tests superados**.

En VS Code, la configuración incluida en `.vscode/settings.json` ya activa pytest sobre la carpeta raíz, así que los tests aparecen directamente en la pestaña *Testing*.

---

## Benchmarking y profiling

`imatlab_benchmark.py` mide con `timeit` el tiempo medio de ejecución por lotes (100 repeticiones, constante `NITERS`) y genera un perfil con `cProfile`. Los ficheros a medir se seleccionan editando las listas `in_files` y `out_files` del bloque `__main__`; las rutas son relativas al directorio desde el que se ejecuta el script, así que hay que lanzarlo desde `tests/` o anteponer `tests/` a los nombres.

Tiempos de referencia del enunciado (medidos en los laboratorios de ICAI):

| Fichero | Bronce | Plata | Oro |
|---|---|---|---|
| `primosTest.txt` | 10 s | 4,3 s | 730 ms |
| `factorTest.txt` | 7,5 s | 2,33 s | 1,99 s |
| `mcdTest.txt` | 2,7 s | 1,5 s | 1 s |
| `potenciaTest.txt` | 800 ms | 220 ms | 120 ms |
| `invTest.txt` | 6,5 s | 4,2 s | 3,125 s |
| `eulerTest.txt` | 5,5 s | 1,06 s | 779 ms |
| `sistemaTest.txt` | 4,5 s | 1,5 s | 988 ms |
| `cuadraticaTest.txt` | 1,1 s | 355 ms | 218 ms |

Los tiempos oficiales se toman en los ordenadores de ICAI con `imatlab_benchmark.py`; cualquier medición en otra máquina es solo orientativa.