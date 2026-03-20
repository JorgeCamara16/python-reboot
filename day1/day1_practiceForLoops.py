# for loops = execute a block of code a fixed number of times.
#             I can iterate over a range, sring, secuence, list, etc.

"""
Basic syntax:
for variable in sequence:
    # code to execute

Example:
for i in range(5):
    print(i)

#If i want to see the numbers in a line, i can use the word end in the print function, it will change the default behavior of the print function, which is to add a new line after each print statement, and instead it will add a space after each print statement, so we can see the numbers in a line. I can also use any other character instead of a space, for example, a comma or a dash.
for i in range(5):
    print(i, end=" ") #end = end of line, it changes the default behavior of the print function, which is to add a new line after each print statement, and instead it will add a space after each print statement, so we can see the numbers in a line.

# for loop with a list
productos = ["laptop", "mouse", "teclado"]
for i in productos:
    print(i) 

# for loop with a range
for i in range(1, 11):
    print(i)

# reversed for loop
for i in reversed(range(1, 11)):
    print(i)
print("¡Feliz año nuevo!")

#If I add a third parameter to the range function, I can specify the step size (literalmente el salto que da el contador):
for i in range(0, 11, 2):
    print(i)

# i can read a string with a for loop
creditCard = "1224-5678-9012-3456"
for i in creditCard:
    print(i)

#nested for loop, it's a for loop inside another for loop, it's useful when we want to iterate over a sequence of sequences, for example, a list of lists, or a matrix.
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")
  
# Also, there are some specific words that we can use in a for loop, like break, continue, and else.
# break: it will exit the loop when a certain condition is met.
for i in range(1, 11):
    if i == 5:
        break
    else:
        print(i)

# continue: it will skip the current iteration when a certain condition is met.
for i in range(1, 11):
    if i == 5:
        continue # it will skip the number 5 and continue with the next iteration until it reaches 10.
    else:
        print(i)

# else: it will execute a block of code when the loop is finished, but only if the loop was not terminated by a break statement.
#else:
    #print("Loop finished without encountering a break statement.")


#Examples:
#1. Print the five tables using a for loop.
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

"""  

#2. sum of n numbers using a for loop, i'm gonna ask the user to input the number.
n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total += i
print(f"Sum of {n} numbers: {total}")