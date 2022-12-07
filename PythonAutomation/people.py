class Person():
    """Creating a man"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100


    def description_person(self):
        """ Получение описания человека"""
        description = self.name + ", ему  " + str(self.age) + ", его рост " + str(self.height) + ", его вес " + str(self.weight)
        print("Нового человека зовут: " + description)

    def getWeight(self):
        """Получение весе человека"""
        print("Вес нашего человека: " + str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека """
        self.weight = kg

class Warrior(Person):
    """Создаем класс Воина"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение заряда ярости"""
        print("Заряд ярости равен: " + str(self.rage))

    def description_person(self):
        """ Переопределение метода родителя"""
        description = self.name + ", ему  " + str(self.age) + ", его  заряд ярости " + str(self.rage)
        # print("Нового человека зовут: " + description)
        return description



warrior = Warrior("Konan", 32, 200)
warrior.update_weight(130)
warrior.description_person()

warrior.get_rage()

man = Person('Kolya', 30, 180)
man.description_person()
man.weight = 80
# man.update_weight(85)
# man.getWeight()

print('Нового человека зовут: ' + warrior.description_person())
