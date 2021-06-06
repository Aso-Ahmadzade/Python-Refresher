def devide(dividend, divisor):
    return dividend / divisor


# __name__ is a global variable in Python that changes depending on which file you're in. So only the file we're run is __main__. And as soon as you import other files, Python will name them according to their path.
print("module_1.py: ", __name__)


import lib.mudule_2