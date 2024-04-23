class Pet:
    def __init__(self, name):
        self. name = name

    def

class Dog(Pet):

    dog_count = 0
    def __init__(self, name, breed="Mixed"):
        super().__init__(name)
        self.breed = breed
        Dog.dog_count += 1  #

    def sound(self):

        print(f"{self.name} barks: Woof!")

    def type(self):
        print(f"I am a Dog (also a Pet).")

    def get_dog(self):
        return Dog.dog_count





dog1 = Dog("Azor", "Kok")
print(dog1.get_dog())
print(dog1.sound())


