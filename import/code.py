from module_1 import devide
import sys

print(devide(15, 5))

print(__name__)


# So how does Python know where mymodule is? The answeri is in import sys. And we use sys.path .

print(sys.path)
print(sys.modules)