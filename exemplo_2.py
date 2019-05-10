"""
Tutorial-annotations-pyte-hints-live-84

Tutorial for annotations with python

Homepage and documentation:
https://github.com/kivy-tutorial/Tutorial-annotations-pyte-hints-live-84

License: GNU GENERAL PUBLIC LICENSE Version 3
"""

# Modificação 1

# '1' + 1

'''
# Modificação 2

def soma(x, y):
    """ Função soma - não tem error no mypy"""
    return x + y

print(soma('x', 'y'))

print(soma(1, 2))

print(soma(1.0, 2.0))
'''
'''
# Modificação 3

def soma(x: int, y):
    """ Função soma - não tem error no mypy"""
    return x + y

print(soma('x', 'y'))

print(soma(1, 2))

print(soma(1.0, 2.0))
'''

'''
# Modificação 4

from typing import Union

def soma(x: Union[int, float], y):
    """ Função soma - não tem error no mypy"""
    return x + y

print(soma('x', 'y'))

print(soma(1, 2))

print(soma(1.0, 2.0))

print(soma(1.0+1j, 2.0))
'''

'''
# Modificação 5

from typing import Union

def soma(x: Union[int, float], y: str):
    """ Função soma - não tem error no mypy"""
    return x + y

print(soma('x', 'y'))

print(soma(1, 2))

print(soma(1.0, 2.0))

print(soma(1.0+1j, 2.0))
'''

'''
# Modificação 5

from typing import Union

def soma(x: Union[int, float, str], y: Union[int, float]) -> Union[int, float, None]:
    """ Função soma - não tem error no mypy"""
    
    # verify if x is string
    if isinstance(x, str):
        return None
    return x + y


print(soma(1, 2))

print(soma('batatas', 2))

print(soma(1.0, 2.0))
'''

# Modificação 6

from typing import Union, Optional

def soma(
         x: Union[int, float, str], 
        #  y: Union[int, float]
         y: float
    ) -> Optional[float]:
    """ Função soma - não tem error no mypy"""
    
    # verify if x is string
    if isinstance(x, str):
        return None
    return x + y


print(soma(1, 2))

print(soma('batatas', 2))

print(soma(1.0, 2.0))
