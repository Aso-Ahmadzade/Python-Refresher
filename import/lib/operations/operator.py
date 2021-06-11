# .. means accessing the parent folder (lib folder) in Python. And then go to mylib file and import everything from there.
from ..mylib import *

print("operator.py: ", __name__)


def say_bye():
    pass
