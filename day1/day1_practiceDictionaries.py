# dictionary = is a collection of {key:value} pairs ordered and changeable. No duplicates.

capitals = {"USA": "Washington D.C.",
            "India": "New Deli",
            "China": "Beijing",
            "Russia": "Moscow"}
#print(capitals) #to print the dictionary in a line

#Like always, we can use the next functions:
#print(dir(capitals)) #to see the different attributes we can use with a dictionary
#print(help(capitals)) #to see the description of those attributes

#print(capitals.get("Russia")) #to get the value associated with that key 
# If we search for an item that isn't in the dictionary, we'll get "none", kind of "state" that we can use, for example:
"""
if capitals.get("China"):
    print("That capital exists")
else:
    print("I don't know that Country")
"""
#update a dictionary
#This function can add a new key:value in the dictionary or update an existing key:value pair
"""
capitals.update({"Germany": "Berlin"})
print(capitals)

capitals.update({"USA": "Miami"})
print(capitals)
"""

# Also, wa can use the pop method
"""
capitals.pop("USA") #to delete a specific key or
capitals.popitem() #in this case, it'll delete the last pair
capitals.clear() #to delete all the items
print(capitals)
"""

#to get all of the keys within the dictionary but not the values
"""
keys = capitals.keys() #we can use these values to make a for loop
#print(keys)
for key in keys:
    print(key)

#without an initialized variable
for key in capitals.keys():
    print(key)
"""

#We can get just the values
"""
#print(capitals.values())

for value in capitals.values():
    print(value)
"""

#We have the las point to work with dictionaries: "ITEMS".
"""
items = capitals.items() #it changes each "pair {key: value}" in a tuple, so now the dictionary It's kind of "list of tuples"
print(items)

#We can use a for loop to iterate each item
for key, value in capitals.items(): #in this case we have two counters because of the dictionary
    print(f"{key}: {value}")
"""

#Exercises

producto = {
    "nombre": "Laptop",
    "precio": 15000,
    "stock": 10
}

print(f"Producto: {producto.get('nombre')}") #I'll use single quote marks 'cause I dont't want to confuse Python
print(f"Precio: {producto.get('precio')}")
print(f"Stock: {producto.get('stock')}")
