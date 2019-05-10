"""
Tutorial-annotations-pyte-hints-live-84

Tutorial for annotations with python

Homepage and documentation:
https://github.com/kivy-tutorial/Tutorial-annotations-pyte-hints-live-84

License: GNU GENERAL PUBLIC LICENSE Version 3
"""

'''
# Modificação 1

from typing import Callable, Sequence, Generator

def soma_1(x: int) -> int:
    """ Função soma 1"""
    return x + 1


def mymap(f: Callable, l: Sequence) -> Generator:
    """ Função mymap"""
    return (f(x) for x in l)

# l é uma lista
print(mymap(soma_1, [1, 2, 3]))

# l é uma tupla
print(mymap(soma_1, (1, 2, 3)))

# l é uma string
print(mymap(soma_1, '1 2 3'))
'''


'''
# Modificação 2

from typing import Callable, Sequence, Generator, Union, Dict, List, Tuple


def soma_1(x: int) -> int:
    """ Função soma 1"""
    return x + 1


def mymap(f: Callable, l: Union[Tuple, List, Dict]) -> Generator:
    """ Função mymap"""
    return (f(x) for x in l)

# l é uma lista
print(mymap(soma_1, [1, 2, 3]))

# l é uma tupla
print(mymap(soma_1, (1, 2, 3)))

# l é uma string
print(mymap(soma_1, '1 2 3'))
'''

'''
# Modificação 3

from typing import Callable, Sequence, Generator, Union, Dict, List, Tuple


def soma_1(x: int) -> int:
    """ Função soma 1"""
    return x + 1


def mymap(f: Callable, l:List[str]) -> Generator:
    """ Função mymap"""
    return (f(x) for x in l)

# l é uma lista
print(mymap(soma_1, [1, 2, 3]))

# # l é uma tupla
# print(mymap(soma_1, (1, 2, 3)))

# # l é uma string
# print(mymap(soma_1, '1 2 3'))
'''

'''
# Modificação 4

from typing import Callable, Sequence, Generator, Union, Dict, List, Tuple


def soma_1(x: int) -> int:
    """ Função soma 1"""
    return x + 1


def mymap(f: Callable, l: Tuple[int, int, int]) -> Generator:
    """ Função mymap"""
    return (f(x) for x in l)

# l é uma lista
# print(mymap(soma_1, [1, 2, 3]))

# l é uma tupla
print(mymap(soma_1, (1, 2, 3)))

# l é uma string
# print(mymap(soma_1, '1 2 3'))
'''

'''
# Modificação 5

from typing import Callable, Sequence, Generator, Union, Dict, List, Tuple


def soma_1(x: int) -> int:
    """ Função soma 1"""
    return x + 1


# def mymap(f: Callable, l: Dict[str, int]) -> Generator:
def mymap(f: Callable, l: Dict[int, str]) -> Generator:
    """ Função mymap"""
    return (f(x) for x in l)

# l é uma dict
print(mymap(soma_1, {1: 'a', 2: 'b'}))
'''

'''
# Modificação 6

from typing import Callable, Sequence, Generator, Union, Dict, List, Tuple


def soma_1(x: int) -> int:
    """ Função soma 1"""
    return x + 1


def mymap(
    f: Callable, 
    # l: Union[List, Tuple, Dict]
    l: Union[List[int], Tuple[int, int, int], Dict[int, str]]
) -> Generator:
    """ Função mymap"""
    return (f(x) for x in l)

# l é uma lista
print(mymap(soma_1, [1, 2, 3]))

# l é uma tupla
print(mymap(soma_1, (1, 2, 3)))

# l é uma dict
print(mymap(soma_1, {1: 'a', 2: 'b'}))
'''


'''
# Modificação 7

from typing import Callable, Sequence, Generator, Union, Dict, List, Tuple

# Alias
Alias = Union[List[int], Tuple[int, int, int], Dict[int, str]]

def soma_1(x: int) -> int:
    """ Função soma 1"""
    return x + 1


def mymap(
        f: Callable, 
        l: Alias
    ) -> Generator: 
    """ Função mymap"""
    return (f(x) for x in l)

# l é uma lista
print(mymap(soma_1, [1, 2, 3]))

# l é uma tupla
print(mymap(soma_1, (1, 2, 3)))

# l é uma dict
print(mymap(soma_1, {1: 'a', 2: 'b'}))
'''

# Modificação 8

from typing import Callable, Sequence, Generator, Union, Dict, List, Tuple

# Alias
Alias = Union[List[int], Tuple[int, int, int], Dict[int, str]]

def soma_1(x: int) -> int:
    """ Função soma 1"""
    return x + 1


# def xpto(x: str) -> int:
def xpto(x: str) -> str:
    """ Função soma 1"""
    # return x + 1  # error
    return x + 'xpto'


def mymap(
        # f: Callable,
        f: Callable[[int], int],
        l: Alias
    ) -> Generator: 
    """ Função mymap"""
    return (f(x) for x in l)

# l é uma lista
print(mymap(soma_1, [1, 2, 3]))

# l é uma tupla
print(mymap(soma_1, (1, 2, 3)))

# l é uma dict
print(mymap(soma_1, {1: 'a', 2: 'b'}))

# função xpto
# print(mymap(xpto, [1, 2, 3]))  # error
