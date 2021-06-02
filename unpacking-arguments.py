# *args is just a variable name that will be used to collect the
#  arguments.
def multiply(*args):
	total = 1
	for arg in args:
		total *= arg
	return total

print(multiply(1, 2, 3))


def add(x, y):
	return x + y

print(add(x=8, y=4))

nums = [8, 4]
# Destructure arguments into multiple parameters using *.
print(add(*nums))

numbers = {"x": 15, "y": 29}
print(add(numbers["x"], numbers["y"]))
print(add(x=numbers["x"], y=numbers["y"]))

# We can use ** for destructure arguments into multiple parameters from a
# dictionary. Note that for using this feature, we should use the same key
# name inside our dictionary that we have used for naming our arguments
# inside our function. I mean x and y.
print(add(**numbers))


def apply(*args, operator):
	if operator == "*":
		# Here, we should pass *args instead of args to the multiply function.
		# Because we give these individual numbers <1, 3, 8, 4> to the apply
		# function and *args in apply function collect the numbers and
		# convert them to a tuple (1, 3, 8, 4). So if we use args in our
		# multiply function, this means that we pass a tuple to multiply
		# function. And if we look at the definition of multiply function we
		# see that, we used *args and it means that it collect the items and
		# convert them to a tuple ((1, 3, 8, 4), ) that is a tuple of a tuple
		# and the result would be (1, 3, 8, 4). So for solving this problem
		# we passed *args to our multipy function. So at first it destructure
		# the tuple of numbers into multiple numbers <1, 3, 8, 4> and then at
		# the definition of multiply function that we used *args and it
		# collect the numbers and convert them to a tuple (1, 3, 8, 4). 
		return multiply(*args)
	elif operator == "+":
		return sum(args)
	else:
		return "No Valid operator provided to apply()."


print(apply(1, 3, 8, 4, operator="*"))