class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def object_info(self):
		return self

	@classmethod
	def class_info(cls):
		return cls


scorpion = Person("scorpion", 35)

print(scorpion)
print(scorpion.object_info())
print(scorpion.class_info())



class Animal:
	def __init__(self, name, age):
		self.name = name
		self.age = age


	# This method gets called for you, when you want to turn your object into
	# a string. The string is Line 31 here. Also we can use this method like
	# this: str(name_of_object)
	def __str__(self):
		return f"Animal {self.name}, {self.age} years old"

	# Although we returned self but unlike what we saw in Person class, Here
	# the result is Line 31, Because we used __str__ magic method.
	def object_info(self):
		return self

	@classmethod
	def class_info(cls):
		return cls


eagle = Animal("Eagle", 7)

print(eagle)
print(str(eagle))

print(eagle.object_info())
print(eagle.class_info())


class Fruit:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# Note that if you want to use __repr__ magic method, you shouldn't
	# use __str__ magic method. Because in that case we just see the result
	# of __str__ method and we can't see the out put of __repr__ method. So
	# don't use them in a class at the same time.

	# The goale of __repr__ method is to be unambiguous, and if possible it
	# should return a string that allows us to recreate the original object
	# very easily.
	def __repr__(self):
		return f"Fruit('{self.name}', {self.age})"

	# Although we returned self but unlike what we saw in Person class, Here
	# the result is Line 60, Because we used __repr__ magic method.
	def object_info(self):
		return self

	@classmethod
	def class_info(cls):
		return cls


apple = Fruit("Apple", 1)

print(apple)
print(apple.object_info())
print(apple.class_info())

