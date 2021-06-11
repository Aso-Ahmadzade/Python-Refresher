from lib.operations import operator

print("mylib.py: ", __name__)


# When you are trying to do a relative import, what Python is gonna to do is, it's going to remove the file (Here the file is <mylib>) and it's just going to try append whatever you import from into the rest of the import path.

# Here, we don't get any error. Because it say's: Ok mylilb, you are inside lib.mylilb, so because you're going to do a relative import, we're going to remove the file and we're gonna try to put operations.operator at the end and import from there. So here it'll work, because it'll do lib.operations.operator and then it'll import say_bye function from that.

# However it will work, when we run it from mycode.py file. If by any reason we want to run our mylib.py file for example to debug it, we won't be able to. Because, of course this now becomes __main__ and we can't use relative imports inside it.
 
from .operations.operator import say_bye
print("mylib.py: ", __name__)

def say_hello():
    pass


# So if you are going to use relative imports, you always have to run the same file at the top level. Otherwise you may encounter some issues.