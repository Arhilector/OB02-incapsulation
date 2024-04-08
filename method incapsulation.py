class Test():
    def public_function(self):
        return "публичная функция"

    def _protected_function(self):
        return "защищенная функция"

    def __private_function(self):
        return "приватная функция"


    def test_private(self):
        return self.__private_function() #добавили функцию вывода приватных данны


object = Test()

object.public_function()
object._protected_function()
object.test_private()
