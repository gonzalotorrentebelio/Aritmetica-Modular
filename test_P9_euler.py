import pytest
import modular
from test_imatlab import try_command

@pytest.mark.parametrize("n,salida_esperada",[
    (7,6),
    (15,8),
    (10,4),
    (13,12),
    (16,8),
    (36,12),    
])
def test_euler_basico(n: int, salida_esperada: int) -> None:
    assert(modular.euler(n)==salida_esperada)

@pytest.mark.parametrize("n,salida_esperada",[    
    (7,"6"),
    (15,"8"),
    (10,"4"),
    (13,"12"),
    (16,"8"),
    (36,"12"), 
])
def test_euler_imatlab(n: int, salida_esperada: str) -> None:
    try_command(f"euler({n})",salida_esperada)