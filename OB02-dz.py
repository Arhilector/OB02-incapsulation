#Разработай систему управления учетными записями пользователей для небольшой компании. К
# омпания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и
# могут добавлять или удалять пользователя из системы.

#Требования:

#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа
# ('user' для обычных сотрудников).

#.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).

#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name
        self.__access_level = "user"
        self.__private = None

    def get_name(self):
        return self.__name

    def get_private(self):
        return self.__private

    def set_private(self, value):
        self.__private = value


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.users = []  # Список всех пользователей

    def add_user(self, user):
        self.users.append(user)
        print(f"{user.get_name()} добавлен в список сотрудников")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.get_name()} удален из списка сотрудников")
        else:
            print("Такого пользователя не найдено!")

    def show_users(self):
        for user in self.users:
            print(user.get_name())


# Создаем объекты
admin = Admin(1, 'Админ Вася')
user1 = User(2, 'Пользователь Петя')
user2 = User(3, 'Пользователь Додик')
user3 = User(4, 'Пользователь Нина')
admin2 = Admin(5, 'Админ Ахмет')

# Использование методов
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(admin2)
admin.remove_user(user1)
print("СПИСОК СОТРУДНИКОВ: ")
admin.show_users()

user2.set_private("теперь его зовут махмут")
print(user2.get_private())







