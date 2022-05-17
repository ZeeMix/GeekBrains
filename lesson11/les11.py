
# Статические методы @staticmethod
class Auto:
    @staticmethod
    def get_class_info():
        print('Детальная информация о классе')


Auto.get_class_info()


# class MyClass:
#     @staticmethod
#     def on_sum_1(param1, param2):
#         return param1 + param2
#
#     def on_sum_2(self, param_1, param_2):
#         return param_1 + param_2
#
#     def on_sum_3(self, param_1, param_2):
#         return MyClass.on_sum_1(param_1, param_2)
#
#
# print(MyClass.on_sum_1(20, 40))
# mc = MyClass()
# print(mc.on_sum_2(20, 20))
# print(mc.on_sum_1(50, 50))
# print(mc.on_sum_3(60, 60))

# @classmethod
# class MyClass:
#     @classmethod
#     def my_method(cls, param):
#         print(cls, param)
#
#
# MyClass.my_method(30)
# mc = MyClass()
# mc.my_method(50)


# Атрибуты и встроенные методы
# class User:
#     def __init__(self, name, login, passwd, email):
#         self.name = name
#         self.login = login
#         self.passwd = passwd
#         self.email = email
#
#     def on_get_data(self):
#         print(f"имя: {self.name}, логин: {self.login}, "
#         f"пароль: {self.passwd}, email: {self.email}")
#
#
# u = User("Ivan Ivanov", "IvIv", "11111", "iviv@mail.ru")
# u.on_get_data()
# print(f"__name__ - {User.__name__}, \n __module__ - {User.__module__}, \n"
# f"__dict__ - {User.__dict__}, \n __bases__ - {User.__bases__}, \n"
# f"__doc__ - {User.__doc__}, \n __class__ - {User.__class__}, \n"
# f"__init__ - {User.__init__}, \n __hash__ - {User.__hash__}")


class Persona:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Name and surname: {self.name} {self.surname}"


class Teacher(Persona):
    def to_teach(self, subj, *pupils):
        for pupil in pupils:
            pupil.to_take(subj)


class Pupil(Persona):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledges = []

    def to_take(self, subj):
        self.knowledges.append(subj)


class Subject:
    def __init__(self, *subjects):
        self.subjects = list(subjects)

    def my_list(self):
        return self.subjects


s = Subject('maths', 'physics', 'biology')
t = Teacher('Ivan', 'Ivanov')
print(t)
p_1 = Pupil('Petr', 'Petrov')
p_2 = Pupil('Sergey', 'Sergeev')
p_3 = Pupil('Vladimir', 'Vladimirow')
print(f"{p_1}, {p_2}, {p_3}")

t.to_teach(s, p_1, p_2, p_3)
print(p_1.knowledges[0].my_list())

