#Dictionaries
dog = {'name': 'Roger', 'age': 8, 'color': 'green'}

#print(list(dog.items()))

#print(len(dog))

dog['favorite food'] = 'Meat'

del dog['color']

dogCopy = dog.copy()

#print(dog)

# sets
set1 = {'sab', 'kailtin'}
set2 = {'sab'}

#intersect = set1 & set2
mod = set1 | set2
#print(intersect)
#print(mod)

#Functions
def hello(name, age):
    
    print('Hello ' + name + ', you are '+ str(age) + ' years old!')
hello('Sab', 24)   

age = 8
print(age.real)
print(age.imag)
print(age.bit_length())

items = [1, 2]
items.append(3)
items.pop()
print(id(items))

count = 0
while count < 10:
    print("the condition is True")
    count += 1

print ("after the loop")

item = [1, 2, 3, 4]
for index, item in enumerate(item):
    print(index, item)