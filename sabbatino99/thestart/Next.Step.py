#Dictionaries
#dog = {'name': 'Roger', 'age': 8, 'color': 'green'}

#print(list(dog.items()))

#print(len(dog))

#dog['favorite food'] = 'Meat'

#del dog['color']

#dogCopy = dog.copy()

#print(dog)

# sets
#set1 = {'sab', 'kailtin'}
#set2 = {'sab'}

#intersect = set1 & set2
#mod = set1 | set2
#print(intersect)
#print(mod)

#Functions
#def hello(name, age):
    
#    print('Hello ' + name + ', you are '+ str(age) + ' years old!')
#hello('Sab', 24)   

#age = 8
#print(age.real)
#print(age.imag)
#print(age.bit_length())

#items = [1, 2]
#items.append(3)
#items.pop()
#print(id(items))

#count = 0
#while count < 10:
    #print("the condition is True")
#    count += 1

#print ("after the loop")

#item = [1, 2, 3, 4]
#for index, item in enumerate(item):
    #print(index, item)


##Classes example

#class Animal:
#    def walk(self):
#        print('Walking....')

#class Dog(Animal):
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

  #  def bark(self):
 #       return('woof')

#kiko = Dog('kiko', 3)

#print(kiko.name)
#print(kiko.age)

#print(kiko.bark())
#kiko.walk()

##Modules

#import math

#print(math.sqrt(100))

#lambda functions

#lambda num : num * 2

#multiply = lambda a, b : a * b
#print(multiply(2, 4))

# map, filter, rereduce
#map()
#numbers = [1, 2, 3]

#result = map(lambda a : a * 2, numbers)

#print(list(result))

#filter()

#numbers = [1, 2, 3, 4, 5, 6]

#result = filter(lambda n : n % == 0, numbers)

#print(list(result))

#reduce()
#from functools import reduce
#expenses = [
#    ('Dinner', 80),
#    ('Car Repair', 120)
#]

#sum = reduce(lambda a, b: a[1] + b[1], expenses)

#print(sum)

#Recursion

#def factorial(n):
#    if n == 1: return 1
#    return n * factorial(n-1)

#print(factorial(3))
#print(factorial(4))
#print(factorial(5))

#Decorators
#def logtime(func):
#    def wrapper():
#        print('before')
#        val = func()
#        print('after')
#        return val
#    return wrapper

#@logtime
#def hello():
#    print('hello')

#hello()

##Docstring

#def increment(n):
#    '''Increment a number'''
#    return n + 1

#class Dog:
#    '''A class representing a dog'''
#    def __init__ (self, name, age):
#        self.name = name
#        self.age = age

#    def bark(self):
#        '''Let the dog bark'''
#        print('WOF!')

#print(help(Dog))

##Annontations

#def increment(n int) -> int:
#    return n + 1

#count: int = 0

##Exections

#try:
    #some lines of code
#except <ERROR1>:
    # handler <ERROR1>
#except <ERROR2>:
    #handler <ERROR2>

#try:
#    result = 2 / 0
#except ZeroDivisionError:
#    print ('Cannot divid by zero!')
#finally:
#    result = 1

#print(result) # 1

#try:
#    raise Exception ('An Error!')
#except Exception as error:
#    print(error)

#class DogNotFoundException(Exception):
#    print('inside')
#    pass

#try:
#    raise DogNotFoundException()
#except DogNotFoundException:
#    print('dog not found!')

## list comprehensions

#numbers = [1 , 2, 3, 4, 5]

#numbers_power_2 = [n**2 for n in numbers]
#print (numbers_power_2)

##Polymorphism

#class Dog:
#    def eat(self):
#        print('Eating dog food')

#class Cat:
#    def eat(self):
#        print('Eating cat food')

#animal1 = Dog()
#animal2 = Cat()

#animal1.eat()
#animal2.eat()

## Operator Overloading

class Dog:
    #the Dog Class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False
    
roger = Dog('Roger', 2)
syd = Dog ('Syd', 6)
