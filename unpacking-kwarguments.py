def info(name, age):
	print(name, age)


details = {"name": "Aso", "age": 21}

# For printing values
info(**details)
# For printing keys
info(*details)


def named(**kwargs):
	print(kwargs)

named(**details)


def print_nice(**kwargs):
	named(**kwargs)
	for arg, value in kwargs.items():
		print(f"{arg}: {value}")


print_nice(name="Aso", age=21)







