from lib import mylib

print("mymodule.py: ", __name__)


def devide():
    pass

# from .lib.mylib import say_hello
# If we do this, we get this error: ImportError: attempted relative import with no known parent package.

# So mymodule.py has no information about the folder it's in. So Python can't do a relative import from it.

