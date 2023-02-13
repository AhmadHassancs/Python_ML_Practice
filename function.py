# def func():
#     return 'hello world'    # function definition
#
# func()           # function call


# def this(a):
#     print(a)
#
# this('hello')


# def that(a, b):
#     print(f"the value you inserted for a during function call is {a}")
#     print(f"The value you inseted for b during function call is {b}")
# that(12, 13)

# def sum(a, b):
#     c = a + b
#     return c
#     # print(c)
# d = int(input("enter 1st number: "))
# e = int(input("enter 2nd number: "))
#
# print(sum(d, e))
# sum(1, 2)

# implemet the student grading problem using funtions
# implement the remaining operators in a calculator.

# def abc(param1, param2):
#     if param1 == 1 and param2 == 1:
#         print("Welcome")
#     else:
#         print('you are not welcomed')
#
# a = int(input('please enter a number'))
# b = int(input('please enter another number'))
#
# # abc(param1=1, param2=1)
# abc(param1=a, param2=b)

# def that(a):
#     for i in a:
#         print(i)
#         # return i
#
# b = input("please enter 5 numbers")
# b = list(b)
# that(b)

# def my_name(first_name): # this is function definition
#     print("your first name is " , first_name)
#
# my_name(12) # calling a funtion
# my_name('ahmad')
# my_name(12.123)

# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#
# my_function("Emil", "Tobias", "Linus")

# def my(a, b, c):
#     print(f'the value of a is {a}',
#           f"the value of b is {b}")
#
# my(a = 1, b = 2, c = 3)

# def that(**this):
#     print(f'this at index 0 = {this["index1"]} \n',
#           f'this at index 1 = {this["index2"]} \n',
#           f'this is index 2 = {this["index3"]}')
#
# that(index1 = 'i am at index 0', index2 = 'i am at index 1', index3=12)

# def my_fun(**crazy):
#     print('i am going to take arguments from a dictinary',
#           f'value at key 1 = {crazy["K1"]} \n',
#           f'value at key 2 = {crazy["K2"]} \n',
#           f'the value at key 2 = {crazy["K3"]} \n')
#
# # this_dict = {"K1": 11, "K2": 22}
# my_fun(K1=12, K2=34, K3=56, K4=78)

# def my_fun(**crazy):
#     return crazy["K1"]
#
# # this_dict = {"K1": 11, "K2": 22}
# print(my_fun(K1=12, K2=34, K3=56, K4=78))

# def defaut(a, b, c = 'fun'):
#     print(f'the value u insereted for a = {a} \n',
#           f'the value u inserted for b = {b} \n',
#           f'the default value of c = {c}')
#
# defaut(1, 2, 3)


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(5)

# practice at least 5 examples on recursion, write at least 3 functions each
# to implement *args, **kwargs

# def factorial(n):
#   if n == 1:
#     return 1
#   else:
#     return n * factorial(n-1)
# a = int(input('please enter a number to calculate factorial: '))
# print(factorial(a))

# def sum_list(lst):
#   if len(lst) == 1:
#     return lst[0]
#   else:
#     return lst[0] + sum_list(lst[1:])
#
# print(sum_list([1, 2, 12.2, 4, 5]))
# def find_max(lst):
#   if len(lst) == 1:
#     return lst[0]
#   else:
#     m = find_max(lst[1:])
#     return m if m > lst[0] else lst[0]
#
# print(find_max([11]))

# def this_recurse(a):
#     if a == 1:
#         return a
#     else:
#         a = a * this_recurse(a - 1)
#         return a
#
# print(this_recurse(3))

# write at least 5 recursive functions in python.

# def tri_recursion(k):
#    if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)






