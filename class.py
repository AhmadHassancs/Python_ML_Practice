# a = 'vision'
# print(a)
# print(type(a))

# this = [11, 22, 33, 44]

# class that:    # this is class definition
#     x = 10 + 10  # this is a simple statement in a class
#     y = 10 - 20
#
# a = that()     # making an object of the class named = that
# print(a.x)     # using the statement from the class using object a.
# print(a.y)

# class myclass:
#     def __init__(self, name, age):
#         self.nam = name
#         self.ag = age
#
# a = myclass('vision', 20)
# # b = myclass()
# print(a.ag)
# print(a.nam)

# class abc:
#     def __init__(self, address, prof):
#         self.add = address
#         self.pro = prof
# a = input("enter your address: ")
# b = input("enter your profession: ")
# c = abc(a, b)
# print(f"your address is {c.add}  and your profession is {c.pro}")

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
#   def myfun1(self, address):
#       self.address = address
#       print('my age is ', self.age)
#       print('your address is ', self.address)
#
# p1 = Person("John", 36)
# p1.myfun1('mardan')
# p1.myfunc()

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("John", 36)
# print(p1.age)
# # del p1
# print(p1)


# create a calculator using class and define methods for each operation.
# take values from the user and also decide what the user wants to do.
# create a class the has 3 methods namely, name, address, phone number and takes input from the user
# and prints their values


# class abc:
#     def __init__(self, number1, number2, operation):
#         self.number1 = number1
#         self.number2 = number2
#         self.operation = operation
#         if operation == '+':
#             return print(number1 + number2)
#         elif operation == '-':
#             return print(number1 - number2)
#         elif operation == '/':
#             return print(number1 / number2)
#         elif operation == '*':
#             return print(number1 * number2)
#         else:
#             return print("you have not chosen a valid operation")
#
# a = int(input("enter 1st number: "))
# b = int(input("enter 2nd number: "))
# c = input("choose an operation between \n + \n - \n / \n * \n")
#
# d = abc(a, b, c)

# class calc:
#     def __init__(self, number1, number2, operation):
#         self.number1 = number1
#         self.number2 = number2
#         self.operation = operation
#     def sum(self):
#         return print(f"the sum of {self.number1} and {self.number2} = {self.number1 + self.number2}")
#     def subtract(self):
#         return print(f"the substraction of {self.number1} and {self.number2} = {self.number1 - self.number2}")
# a = int(input("enter 1st number: "))
# b = int(input("Enter another number: "))
# c = input("choose an operation between + and - ")
#
# if c == '+':
#     d = calc(a, b, c)
#     d.sum()
# else:
#     d = calc(a, b, c)
#     d.subtract()

# complete the calculator with specif methods for division and multiplication

# class abc:
#     def __init__(self, name, address, phone):
#         self.name = name
#         self.address = address
#         self.phone = phone
#         print(f'your name is {self.name}, your address is {self.address} and your contact is {self.phone}')
#
#     # def my_info(self):
#     #     print(f'your name is {self.name}, your address is {self.address} and your contact is {self.phone}')
#
# a = input('enter your name: ')
# b = input("enter your address: ")
# c = input("enter your phone number: ")
#
# d = abc(a, b, c)
# d.my_info()

# inheritance
# class person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def printname(self):
#         print(self.first_name, self.last_name)
# #
# # # a = person('vision', 'institute')
# # # a.printname()
# #
# # class student(person):
# #     def address(self, address):
# #         self.address = address
# #         print(address)
# #
# # b = student('said', 'muhammad')
# # b.printname()
# # b.address('mardan')
#
# class student(person):
#     def __init__(self):
#         print('i am from the inherited init method!')
#
# a = student()
# a






