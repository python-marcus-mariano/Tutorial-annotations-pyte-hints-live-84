"""
Tutorial-annotations-pyte-hints-live-84

Tutorial for annotations with python

Homepage and documentation:
https://github.com/kivy-tutorial/Tutorial-annotations-pyte-hints-live-84

License: GNU GENERAL PUBLIC LICENSE Version 3
"""


'''
# Modificação 1

from minha_lib import soma


soma('str', 'str')
'''

'''
# Modificação 2

from minha_lib import soma


soma('str', 'str')

soma(2, 1)

soma(2.0, 3.0)
'''

# Modificação 3

from minha_lib import soma, sub, div, mult


soma('str', 'str')
soma(2, 1)
soma(2.0, 3.0)
soma(1.1+1j, 1.0)

sub(1, 2)
sub(1, 2.0)
sub(2.0, 3.0)

div(2, 3)
div(1, 1)
div(1, 1.0)


mult('x', 2)
mult(2, 2)
