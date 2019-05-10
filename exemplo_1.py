"""
Tutorial-annotations-pyte-hints-live-84

Tutorial for annotations with python

Homepage and documentation:
https://github.com/kivy-tutorial/Tutorial-annotations-pyte-hints-live-84

License: GNU GENERAL PUBLIC LICENSE Version 3
"""

'''
def concatena(t1, t2):
    """Função concatena."""
    return t1 + t2

result = concatena(1, 1)

print(result)

result = concatena([1], [2])

print(result)

result = concatena((1, 2), (3, 5))

print(result)

print(concatena.__annotations__)
'''

'''
# Modificação 2

def concatena(t1: int, t2: int) -> int:
    """Função concatena - recebe t1 int, t2 int e retorna int."""
    return t1 + t2

result = concatena(1, 1)

print(result)

print(concatena.__annotations__)

print(help(concatena))
'''


'''
# Modificação 3

def concatena(
        t1: [str, int, list, tuple], t2: [str, int, list, tuple]
    ) -> [str, int, list, tuple]:
    """
    Função concatena -
    recebe t1 str ou int ou list ou tuple, t2 str ou int ou list ou tuple
    e retorna str ou int ou list ou tuple.
    """
    return t1 + t2

result = concatena(1, 1)

print(result)

print(concatena.__annotations__)
'''


'''
# Modificação 4

from typing import List, Tuple

def concatena(
        t1: [List, Tuple], t2: [List, Tuple]
    ) -> [List, Tuple]:
    """ Função concatena """
    return t1 + t2

print(concatena.__annotations__)
'''


'''
# Modificação 5

from typing import List, Tuple, Union

def concatena(
        t1: Union[List, Tuple, int], t2: Union[List, Tuple, int]
    ) -> Union[List, Tuple, int]:
    """ Função concatena """
    return t1 + t2

print(concatena.__annotations__)
'''

'''
# Modificação 6

from typing import Any, Union

def concatena(t1: Any, t2: Any) -> Any:
    """ Função concatena - Any returna qualquer coisa """
    return t1 + t2

print(concatena.__annotations__)

def soma_numerica(
        x: Union[int, float, complex],
        y: Union[int, float, complex]
        ) -> Union[int, float, complex]:
    """ Função soma"""
    return x + y
'''

'''
# Modificação 7

from typing import Any, NewType, Dict

# Number = NewType('Number', [int, float, complex])

# muito complexo com new type
# DadosDoCadastro = NewType('Cadastro', Dict[str, str])
# usar Aliar
DadosDoCadastro = Dict[str, str]


def concatena(t1: Any, t2: Any) -> Any:
    """ Função concatena - Any returna qualquer coisa """
    return t1 + t2

print(concatena.__annotations__)

# def soma_numerica(x: Number, y: Number) -> Number:
#     """ Função soma"""
#     return x + y

# print(soma_numerica.__annotations__)

def validar_cadastro(user: DadosDoCadastro) -> bool:
    """ Função validar cadastro"""
    ...

print(validar_cadastro.__annotations__)
'''


# Modificação 8

from typing import Any, TypeVar

Number = TypeVar('Number', int, float, complex)

def concatena(t1: Any, t2: Any) -> Any:
    """ Função concatena - Any returna qualquer coisa """
    return t1 + t2

print(concatena.__annotations__)

def soma_numerica(x: Number, y: Number) -> Number:
    """ Função soma"""
    return x + y

print(soma_numerica.__annotations__)
