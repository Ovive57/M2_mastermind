import sys

__version__ = "0.1"

from . import remplissage

from . import comparaison

__all__ = ['dynamique']  # modules importés par 'import *'

for _mod in __all__:  # imports programmatiques
    __import__(__name__ + '.' + _mod, fromlist=[None])  # ≈ 'from __name__ import _mod'
