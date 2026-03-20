 # nested loops = a loop inside a loop, within another loop (outer, inner)
#                 outer loop:
#                     inner loop:

"""
for i in range (3):
    for j in range (1, 10):
        print(j, end="")
    print() # to move to the next line after the inner loop is done
  
""" 
#Piramids
height = int(input("Enter the height of the pyramid: "))
symbol = input("Enter the symbol for the pyramid: ")

for i in range(height):

    for j in range(height - i - 1):
        print(" ", end="")

    for k in range(2 * i + 1):
        print(symbol, end="")

    print()
 
""" 
# Inverted pyramid
height = int(input("Enter the height of the pyramid: "))
symbol = input("Enter the symbol for the pyramid: ")

for i in range(height):

    for j in range(i):
        print(" ", end="")

    for k in range(2 * (height - i) - 1):
        print(symbol, end="")

    print()

""" 
# Code de pirámide invertida con razonamiento de matriz, donde se define el centro y se determina si la posición actual está dentro del rango de asteriscos o espacios. 
"""
height = int(input("Enter height: "))

center = height - 1
width = height * 2 - 1

for row in range(height):
    for col in range(width):

        if center - row <= col <= center + row:
            print("*", end="")
        else:
            print(" ", end="")

    print()
"""    

# Square pattern
"""  
size = int(input("Enter size: "))

for i in range(size):
    for j in range(size):
        print("*", end="")
    print()

"""      

# Right triangle pattern
"""
size = int(input("Enter size: "))
for i in range(size):
    for j in range (i + 1):
        print("*", end="")
    print()
"""
# Inverted right triangle pattern
"""  
size = int(input("Enter size: "))
for i in range(size):
    for j in range(size - i):
        print("*", end="")
    print()
"""  

# Diamond pattern
""" 
size = int(input("Enter size: "))
for i in range(size):
    for j in range(size - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

for i in range(size - 2, -1, -1):
    for j in range(size - i - 1):
        print(" ", end="")
    for k in range(2*i + 1):
        print("*", end="")
    print()
""" 

# void piramid pattern
""" 
size = int(input("Enter size: "))

for i in range(size):
    for j in range(size - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        if k == 0 or k == 2 * i or i == size - 1: # condition to print "*" only at the borders of the pyramid and the last row
            print("*", end="")
        else:
            print(" ", end="")
    print()
""" 
