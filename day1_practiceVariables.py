print("Soy yo de nuevo, esto apenas y comienza, el infinito es el límite")
# varible = a reusable container for storing a value. A variable behaves as if it were the value it contains. We can use variables to store different types of data, such as strings, integers, floats, and booleans.

#String variables
name = "Jorge"
lastname = "Camara"
state = "Yucatán"
fav_food = "Mole"
fav_language = "Python"
#integer
age = 25
#float
height = 1.75
#Boolean
is_student = True


# Using commas in the print function
#print("Hi, my name is:", name, lastname)
#print("I am", age, "years old")
#print("I am from", state)
#print("My favorite food is", fav_food)
#print("My favorite programming language is", fav_language, "\n\n")

# Using string concatenation
#print("Hi, my name is: " + name + " " + lastname)
#print("I am " + str(age) + " years old")
#print("I'm from " + state)
#print("My favorite food is " + fav_food)
#print("My favorite programming language is " + fav_language + "\n\n")

# Using f-strings (formatted string literals) ---- My preferred method for readability and simplicity
#print(f"Hi, my name is: {name} {lastname}")
#print(f"I am {age} years old")
#print(f"I'm from {state}")  
#print(f"My favorite food is {fav_food}")
#print(f"My favorite programming language is {fav_language}")

#Normally, we use boolean variables in conditional statements to control the flow of the program. For example:

#if is_student:
#    print("I am a student.")
#else:    
#    print("I am not a student.")

# Something interesting, i don't have to use the comparative operator (==) to check the value of a boolean variable, like `is_student == True` (with other lenguages it's necessary), I can just use the variable itself in the condition. If is_student is True, the first block will execute; if it's False, the else block will execute. Python beeing Python, awesome.

#print(f"Am i a student?: {is_student}") 
#When i print the boolean variable, it will show its value (True or False) in the output.

#Multiple variable assignment
name, lastname, age = "Jorge", "Camara", 25
print(f"Hi, my name is: {name} {lastname} and I am {age} years old")

#x, y, z = 1, 2.5, "Hello"
#with the same value
x = y = z = 10
print(x, y, z)