# this = {'name': 'vision', 'age': 12, 'address': 'mardan'}
# print(this)
# # print(type(this))
#
# # print(this['age'])  # extraction
#
# # del this[3]
# # print(this)
#
# this['contact'] = 312123123
# print(this)
#
# a = list(this)
# print(sorted(a))
# print(type(a))
#
# print('vision' not in this)
# a = [('a', 100), ('b', 200), ('c', 300)]
# print(a)
# print(type(a))
# that = dict(a)
# print(that)
# print(type(that))

# a = dict(a = 100, b = 200, c = 300)
# print(a)
# print(type(a))

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# print(thisdict["brand"])

# # ls = [11, 3, 44, 45, 51]
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(len(thisdict))

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict)
# print(type(thisdict))
# print(thisdict['colors'][2])
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": (11, 22, 33, 44)
# }
# print(thisdict)
# print(type(thisdict))
# print(type(thisdict["colors"]))


# this = {'this': 123, 'that': 456, 'him': 789}
# print(this)
# print(type(this))
# z = this.keys()
# print(z)
# print(type(z))


# this = {'this': 123, 'that': 456, 'him': 789}
# print(this)
# print(type(this))
# z = this.values()
# print(z)
# print(type(z))

# this = {'this': 123, 'that': 456, 'him': 789}
# print(this)
# print(type(this))
# z = this.items()
# print(z)
# print(type(z))
# if 'his' in this:
#     print('this key exists in the dictionary')
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# print(type(thisdict))
# thisdict['color'] = 'green'
# print(thisdict)

# a = {'a':1, 'b':2, 'c':3}
# print(a)
# a.update([('d',4),('e',5)])
# print(a)

# a = {'a':1, 'b':2, 'c':3}
# print(a)
# a.update({'d':4, 'e':5})
# print(a)

# that = {'a':1, 'b':2, 'c':3, 'd':4}
# # a = that
# # print(that)
# # a = that.copy()
# # print(a)
# that.fromkeys('a')
# print(that)

# x = ('key1', 'key2', 'key3')
# y = 0
#
# thisdict = dict.fromkeys(x, y)
#
# print(thisdict)
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.setdefault("model")
# y = car.setdefault("color", 'orange')
#
# print(x)
# print(y)
# print("hello world!!")


# print('Hello world and wecome to economics!!')
# a = int(input("enter 1st number"))
# b = int(input("enter 2nd number"))
# print('the sum of a and b is ', a+b)