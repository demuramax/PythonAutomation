class Person():
    """Model of a man"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Man is created')


    def sing(self):
        """Asking the man to sing"""
        print(self.name + ' sings')

    def dance(self):
        """Askin the man to dance"""
        print(self.name + ' dancing')


man = Person("Kolya", 30)
woman = Person('Alice', 28)

print(man.name)
man.sing()
man.dance()
woman.dance()

