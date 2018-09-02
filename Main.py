# author: Xavier Collantes
# date: 09/01/2018
# purpose: Taking py2exe for a spin for Windows ready executable code.
# Dependancies will hopefully be intact.

from distutils.core import setup
import py2exe
setup(console=['myClass.py'])
