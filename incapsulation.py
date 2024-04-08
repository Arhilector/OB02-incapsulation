class Test():
    def __init__(self):
        self.public = "публичный атрибут"

        self._protected = "защищенный атрибут"

        self.__private = "приватный атрибут"

    def get_private(self):
        return self.__private  #запрашиваем значение приватного атрибута

    def set_private(self, value):
        self.__private = value #переписываем значение приватного атрибута



object = Test()
print(object.public)
print(object._protected)


print(object.get_private())

object.set_private("переписали значение приватного атрибута")
print(object.get_private())


