class Test():
    def __init__(self):
        self.public = "публичный атрибут"

        self._protected = "защищенный атрибут"

        self.__private = "приватный атрибут"

    def get_private

object = Test()
print(object.public)
print(object._protected)
print(object.__private)


