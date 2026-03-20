 # Collection = single "variable" used to store multiple values.
 # List = [] ordered a changeable. Duplicate members are allowed.
 # Set = {} unordered an immutable, but Add/remove OK. No duplicate members allowed.
 # Tuple = () ordered and unchangeable. Duplicate members are allowed. FASTER than lists and sets. 
 # Use tuples when you want to store a collection of values that should not be changed, and use lists when you want to store a collection of values that can be changed. Use sets when you want to store a collection of unique values that can be changed.

#All of a list
#List example
cars = ["Lamborguini", "Ferrari", "Porsche", "Bugatti", "McLaren", "Koenigsegg", "Lexus"] #Each value is called an "element". Each element has an "index" starting with 0.
"""
print(f"Your car is a {cars[1]}")
#Experiment with the list methods:
print(cars[0:3]) #Prints the elements from index 0 to 2 (3 is not included).
print(cars[:4]) #Prints the elements from index 0 to 3 (4 is not included).
print(cars[1:]) #Prints the elements from index 1 to the end of the list.
print(cars[::]) #Prints all the elements in the list. The first ":" means to start at the beginning of the list, and the second ":" means to go to the end of the list. The third ":" means to print every element in the list.
print(cars[::-1]) #Prints the elements in reverse order.
print(cars[::-2]) #Prints the elements in reverse order, but only every 2nd element.
print(cars[::2]) #Prints every 2nd element in the list.
print(cars[-1]) #Prints the last element in the list.
print(cars[::3])

#cars.append("McLaren") #Adds an element to the end of the list.

#You can iterate through a list using a for loop:
#When the collection's name is plural, it's usually a good idea to name the variable in singular form when iterating through it. This is just a convention, but it can make your code easier to read.
for car in cars:
    if car == cars[-1]:
      print(car)
    else:
      print(car, end=" - ")

#You can also iterate through a list using a for loop with an index:
for i in range(len(cars)): #The range function generates a sequence of numbers from 0 to the length of the list (not including the length of the list). This is a common way to iterate through a list using an index.
    if i == len(cars) - 1:
        print(cars[i])
    else:
      print(cars[i], end=" - ")


#print(dir(cars)) #Prints all the methods that can be used with the list.
#print(help(cars.append)) #Prints the documentation for the append method.
#print(help(cars)) #Prints the documentation for the list class. This is a very long output, so it's usually better to look up the documentation online.

#print(len(cars)) #Prints the number of elements in the list.
#print("Ferrari" in cars) #Checks if "Ferrari" is in the list. Returns True or False (Boolean).

#cars[3] = "Lamborghini2" #You can change the value of an element in the list by using its index. This is called "mutating" the list. You cannot do this with a tuple, which is immutable.

#cars.append("McLaren") #You can also add an element to the end of the list using the append method. This is also mutating the list.

#cars.remove("McLaren") #You can remove an element from the list using the remove method. This is also mutating the list. Just one element will be removed, even if there are duplicates. It will remove the first occurrence of the element in the list. If the element is not in the list, it will raise a ValueError.

#cars.insert(1, "Lamborghini2") #You can also add an element to the list using the insert method. This is also mutating the list. The first argument is the index where you want to insert the element, and the second argument is the element you want to insert. The element will be inserted at the specified index, and the elements after it will be shifted to the right.

#cars.sort() #You can sort the elements in the list using the sort method. This is also mutating the list. The sort method sorts the elements in ascending order by default, but you can also specify a different sorting order using the reverse parameter. This will sort rhe elements in alphabetical order, but you can also sort the elements in reverse alphabetical order by setting the reverse parameter to True. For example: 
#cars.sort(reverse=True)

#cars.reverse() #You can reverse the order of the elements in the list using the reverse method. This is also mutating the list. The reverse method does not sort the elements in reverse order, it just reverses the order of the elements in the list.

#cars.clear() #You can remove all the elements from the list using the clear method. This is also mutating the list. After calling the clear method, the list will be empty.

#print(cars.index("McLaren")) #You can find the index of an element in the list using the index method. This does not mutate the list. The index method returns the index of the first occurrence of the specified element in the list. If the element is not in the list, it will raise a ValueError.

#print(cars.count("McLaren")) #You can count the number of occurrences of an element in the list using the count method. This does not mutate the list. The count method returns the number of times the specified element appears in the list.

#cars.pop() #You can also remove an element from the end of the list using the pop method. This is also mutating the list. The pop method also returns the element that was removed, so you can store it in a variable if you want to use it later.

print(cars)
"""
#All of a set

#fruits = {"apple", "banana", "orange", "grape", "kiwi", "melon", "watermelon"} 
"""
#Each value is called an "element". Sets are unordered, so they do not have an index. Sets are also mutable, but they do not allow duplicate members. If you try to add a duplicate member to a set, it will not be added.
#We can't count the index of an element in a set, because sets are unordered and do not have an index. However, we can check if an element is in a set using the "in" keyword, which returns a Boolean value (True or False). For example:
#print("apple" in fruits) #This will return True, because "apple" is an element in the set. If we check for an element that is not in the set, it will return False. For example:
#print("pear" in fruits) #This will return False, because "pear" is not an element in the set.
#We can't change the value of an element in a set, because sets are unordered and do not have an index. However, we can add or remove elements from a set using the add and remove methods, which are mutating the set. For example:
#fruits.add("pear") #This will add "pear" to the set. If we try to add "pear" again, it will not be added, because sets do not allow duplicate members.
#fruits.remove("banana") #This will remove "banana" from the set. 
#fruits.pop() #This will remove a random element from the set. 
#fruits.clear() #This will remove all the elements from the set. After calling the clear method, the set will be empty.
print(fruits)
"""

#All of a tuple
"""
fruits = ("apple", "banana", "orange", "grape", "kiwi", "melon", "watermelon")

#We can use the functions (dir, help, len and in), in the same way as the previous collections.
#but we can use only two methods: count and index

#print(dir(fruits))
#print(help(fruits)) 
#print(len(fruits))
#print("aple" in fruits)
#print(fruits.index("kiwi"))
#print(fruits.count("kiwi"))

for fruit in fruits:
    print(fruit)

"""
"""
#Primera versión
numeros = [5, 10, 15, 20]
mayor = numeros[0]
menor = numeros[0]
total = numeros[0]

#Mostrar el mayor
for num in numeros[1:]:
    if  num > mayor:
        mayor = num
print(mayor)

#Mostrar el menor
for num in numeros[1:]:
    if num < menor:
        menor = num
print(menor)

#Mostrar el total
for num in numeros[1:]:
    total = total + num
print(total)
"""
numeros = [5, 10, 15, 20]

#Metámoslo a un solo loop padreeee, WAAAAAAAA

if not numeros:
    print("Lista vacía")
else:
    mayor, menor, total = numeros[0], numeros[0], numeros[0]

    for numero in numeros[1:]: #Para que sea eficiente y no lea con lo que ya está inicializado, empieza del Index 1
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
        total += numero
    print(mayor)
    print(menor)
    print(total)
    
