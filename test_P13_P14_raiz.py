import pytest
import modular
from test_imatlab import try_command

@pytest.mark.parametrize("n,p,salida_esperada1,salida_esperada2",[
    (2,7,3,4),
    (4,7,2,5),
    (9,11,3,8),
    (10,13,6,7),])
def test_raiz_mod_p_basico(n: int, p:int, salida_esperada1: int, salida_esperada2: int) -> None:
    assert(modular.raiz_mod_p(n,p)%p==salida_esperada1 or modular.raiz_mod_p(n,p)%p==salida_esperada2)


def test_raiz_mod_p_no_existe():
    """ Este test comprueba que, en los casos esperados,
    realmente se lanza la excepción esperada"""
    with pytest.raises(modular.IncompatibleEquationError):
        modular.raiz_mod_p(2,5)
    with pytest.raises(modular.IncompatibleEquationError):
        modular.raiz_mod_p(3,7)

    with pytest.raises(modular.IncompatibleEquationError):
        modular.raiz_mod_p(2,11)

    with pytest.raises(modular.IncompatibleEquationError):
        modular.raiz_mod_p(5,7)

@pytest.mark.parametrize("n,p,salida_esperada",[    
    (2,5,"NE"),
    (2,7,"3, 4"),
    (9,3,"0"),
    (4,7,"2, 5"),
    (9,11,"3, 8"),
    (10,13,"6, 7"),
    ])

def test_raiz_imatlab(n: int, p:int, salida_esperada: str) -> None:
    try_command(f"raiz({n},{p})",salida_esperada)



@pytest.mark.parametrize("a,b,c,p,salida_esperada1,salida_esperada2",[
    (4,1,5,11, 3,5),
    (1,2,1,11,10,10),
    (1,0,3,7,2,5),
    (1,4,1,11,3,4),
    (1,6,2,7,4,4),    
])
def test_ecuacion_cuadratica_basico(a:int, b:int, c: int, p:int, salida_esperada1: int, salida_esperada2: int) -> None:
    assert(modular.ecuacion_cuadratica(a,b,c,p)==(salida_esperada1,salida_esperada2) or modular.ecuacion_cuadratica(a,b,c,p)==(salida_esperada2,salida_esperada1))

@pytest.mark.parametrize("a,b,c,p",[
    (4,1,3,11),
    (1,0,1,7),
    (1,1,1,5),
    (1,0,1,11),
    ])

def test_ecuacion_cuadratica_no_existe(a:int, b:int, c: int, p:int) -> None:
    """ Este test comprueba que, en los casos esperados,
    realmente se lanza la excepción esperada"""
    with pytest.raises(modular.IncompatibleEquationError):
        modular.ecuacion_cuadratica(a,b,c,p)

@pytest.mark.parametrize("a,b,c,p,salida_esperada",[    
    (4,1,5,11, "3, 5"),
    (1,2,1,11,"10"),
    (4,1,3,11,"NE"),
    (1,0,3,7,"2, 5"),
    (1,4,1,11,"3, 4"),
    (1,6,2,7,"4"),
    (1,0,1,7,"NE"),
    (1,1,1,5,"NE"),
    ])
def test_ecuacion_cuadratica_imatlab(a:int, b:int, c: int, p:int, salida_esperada: str) -> None:
    try_command(f"ecCuadratica({a},{b},{c},{p})",salida_esperada)
