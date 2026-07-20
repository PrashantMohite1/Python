class Dog:
    def sound(self):
        print("Woof")

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

# One function works with ANY object that has .sound()
def make_it_speak(animal):
    animal.sound()          # doesn't care about the class!

for a in [Dog(), Cat(), Cow()]:
    make_it_speak(a)