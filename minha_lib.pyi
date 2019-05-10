"""
Arquivo de stub (toco, ponta)
"""


'''
# Modificação 1

def soma(x: int, y: int) -> int:
    """ Função soma."""
    ...
'''

'''
# Modificação 2

from typing import Union

def soma(x: Union[int, str], y: Union[int, str]) -> Union[int, str]:
    """ Função soma."""
    ...
'''

'''
# Modificação 3 ***************************

from typing import overload


@overload
def soma(x: int, y: int) -> int:
    """ Função soma."""
    ...

@overload
def soma(x: float, y: float) -> float:
    """ Função soma."""
    ...

@overload
def soma(x: str, y: str) -> str:
    """ Função soma."""
    ...

'''

# Modificação 4

from typing import overload


@overload
def soma(x: int, y: int) -> int:
    """ Função soma."""
    ...

@overload
def soma(x: float, y: float) -> float:
    """ Função soma."""
    ...

@overload
def soma(x: str, y: str) -> str:
    """ Função soma."""
    ...

# erro função mal feito
# @overload
# def soma(x: int, y: float) -> str:
#     """ Função soma."""
#     ...
