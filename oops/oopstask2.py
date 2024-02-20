class Animal:
    def __init__(self, name):
        self.__name = name           # set as private (encapsulation )
    def get_name(self):
        return self.__name

    def speak(self):                # Abstract 
        pass                    

class Dog(Animal):          # inheritance
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"



#polymorphism
    
def make_animal_speak(animal):
    print(f"{animal.get_name()} says: {animal.speak()}")


dog = Dog("Rolex")
cat = Cat("missy")

make_animal_speak(dog)  
make_animal_speak(cat)  