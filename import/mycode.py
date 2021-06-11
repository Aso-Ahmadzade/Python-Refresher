# These are absolute imports, where you have to define the path that you're importing from.

import mymodule

print("mycode.py: ", __name__)


# The relative import is one that can import from the current folder that the file is in but it can not import unless there is a folder name in the import path, in the module path. (From mymodule.py and mycode.py we can't do relative imports. But from mylib.py and mymodule.py we can do relative imports.). 

# lib.operation.operator : lib and operations are folder names and operator is a file name. 
# lib.mylib : lib is a folder name and mylib is a file name.

# So The last ones are file names and names before them that separated by dot (.)are folder names.


# In order to do a relative import, you need to use <from> syntax.

# Here dot (.) means, from the current folder look at the mymodule file and imprt the devide function.
# from .mymodule import devide

# If we do that, we get this error that says: ImportError: attempted relative import with no known parent. Note package and folder means the same thing we're Python source code.

# So because the name of this file was __main__ and it doesn't have a folder, it tries to import from the current place it's in and Python won't let you do that. So if you're importing from the file you run, you can't use relative imports.

