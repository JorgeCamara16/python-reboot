#while loop = execute some code WHILE some condition remains true

"""Example 1, only read one string
name = input("Enter your name: ").strip() #strip() = remove any leading or trailing whitespace from the input, so we don't have to worry about extra spaces before or after the name.

while name == "" or not name.isalpha(): #isalpha() = check if the input contains only letters, so we don't have to worry about numbers or special characters in the name. Also we check if the name is empty, because an empty string is not a valid name. In addition, we can check if the input contains only digits with isdigit() or if it contains only alphanumeric characters with isalnum(), but for a name we want to check if it contains only letters, so we use isalpha().
    print("Invalid input, please enter a valid name.")
    name = input("Enter your name: ").strip() 

print("Hello " + name + "!")

#Example 2, now, i want to read a full name, so i'll use the function split() and a for loop to check if each part of the name is valid. The split() function will split the input into a list of strings, and then we can use a for loop to check if each part of the name is valid.

name = input("Enter your full name: ").strip()

while name == "" or not all(part.isalpha() for part in name.split()):
    print("Invalid input, please enter a valid full name.")
    name = input("Enter your full name: ").strip()

print("Hello " + name + "!")

"""
#Version final, naaaa, it'a lot
"""
while True:
    name = input("Enter your full name: ").strip()

    if len(name.split()) >= 2 and all(part.isalpha() for part in name.split()):
        break
    else:
        print("Invalid input, please enter a valid full name.")

print(f"Hello {name}!")


While not, I used that loop to stay in the loop until we get a valid response, but we can also use a while not loop, which is a more concise way to write the same logic. The while not loop will continue to execute as long as the condition is not true, so we can use it to check for the valid responses and break the loop when the user wants to stop


color = input("Enter your color: ")

while not color == "q":
    print(f"You like {color}!")
    color = input("Enter another color you like (or 'q' to quit): ")

print("Goodbye buddy!")

"""
#Example 3, now i want to read a number between 1 and 10, so i'll use a while loop to check if the input is valid, and if it's not valid, i'll keep asking for input until we get a valid response. We can use the condition num <= 0 or num > 10 to check if the number is outside the valid range, and if it is, we can print an error message and ask for input again. Once we get a valid number, we can break the loop and print a thank you message.
num = int(input("Enter a number between 1 - 10: "))

while num <= 0 or num > 10:
    print("Invalid input, please enter a number between 1 and 10.")
    num = int(input("Enter a number between 1 - 10: "))

print(f"You entered {num}, thank you!")





