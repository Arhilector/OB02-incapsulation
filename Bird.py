
#наследование классов
class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} летает")

    def eat(self):
        print(f"{self.name} кушает")

    def sing(self):
        print(f"{self.name} поет")

    def info(self):
        print(f"Зовут {self.name}, {self.voice} - голос, {self.color} - цвет")


class Golubok(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def walk(self):
        print(f"{self.name} ходит")

    def sing(self):
        print(f"{self.name} поет всякую хуйню")





golubok1 = Golubok("Голубь Педро", "Курлык", "серый̆", "крошки")
golubok1.info()
golubok1.fly()
golubok1.eat()
golubok1.sing()
golubok1.walk()

bird2 = Bird("Кукушка", "куку", "черная")
bird2.info()