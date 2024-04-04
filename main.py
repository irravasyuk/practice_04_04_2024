# Завдання 1
# Задайте метаклас, що автоматично додає
# додатковий функціонал до всіх класів, що його
# використовують.
# class AdditionalFunctionality(type):
#     def __new__(cls, name, bases, dct):
#         dct['additional functionality'] = cls.additional_functionality
#         return super().__new__(cls, name, bases, dct)
#
#     @staticmethod
#     def additional_functionality():
#         print("Додатковий функціонал")
#
# class MyClass(metaclass=AdditionalFunctionality):
#     def __init__(self):
#         pass
#
# my_instance = MyClass
# my_instance.additional_functionality()


# Завдання 2
# Створіть метаклас, що перевіряє наявність певних
# атрибутів у всіх класах, які використовують цей
# метаклас.
# class AttributeCheck(type):
#     attributes = ['attr1', 'attr2']
#
#     def __new__(cls, name, bases, dct):
#         for attr in cls.attributes:
#             if attr not in dct:
#                 raise AttributeError(f'Клас {name} не має атрибуту {attr}')
#
#         return super().__new__(cls, name, bases, dct)
#
# class MyClass(metaclass=AttributeCheck):
#     attr1 = 'hello'
#     attr2 = 'Python'
#     #pass
#
# my_instance = MyClass()


# Завдання 3
# Реалізуйте метаклас, що забороняє спадкування від
# певних класів чи змінює порядок спадкування.
class NoInheritance(type):
    def __new__(cls, name, bases, dct):
        disallowed_classes = [Disallowed1, Disallowed2]

        for base in bases:
            if base in disallowed_classes:
                raise TypeError(f'Спадкування від класу {base.__name__} заборонене.')

        return super().__new__(cls, name, bases, dct)


class Disallowed1:
    pass


class Disallowed2:
    pass


class MyClass(metaclass=NoInheritance):
    pass


try:
    class SubClass(Disallowed1):
        pass
except TypeError as e:
    print(e)

# Завдання 4
# Створіть метаклас, який автоматично реєструє всі
# нові класи у певному реєстрі для подальшого
# використання.
# class ClassRegistry(type):
#     registry = {}
#
#     def __new__(cls, name, bases, dct):
#         new_class = super().__new__(cls, name, bases, dct)
#         cls.registry[name] = new_class
#
#
# class MyClass(metaclass=ClassRegistry):
#     pass
#
#
# print(ClassRegistry.registry)
