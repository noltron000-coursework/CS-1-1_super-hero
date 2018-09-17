class Dog:
	greeting = "Woof!"

	def __init__(self, name):
		self.name = name

	def bark(self):
		print(self.greeting)



if __name__ == "__main__":
	my_dog = Dog("Spot")
	my_other_dog = Dog("Stacy")
	my_dog.bark()
	print(my_dog.name)
	print(my_other_dog.name)

my_first_dog = Dog("Annie")
my_second_dog = Dog("Wyatt")

print(my_first_dog.name)
print(my_second_dog.name)

my_first_dog.bark()
my_second_dog.bark()

my_dogs = list()

my_dogs.append(Dog("Lucky"))
my_dogs.append(Dog("Tofu"))

for dog in my_dogs:
	dog.bark()