class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "Animal Sound"
    
class Elephant(Animal):
    def speak(self):
        return f"{self.name} says 뿌우우"
    
my_elephant = Elephant("Kimchi")

print(my_elephant.speak())