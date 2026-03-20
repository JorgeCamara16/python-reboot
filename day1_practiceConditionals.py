#age = int(input("Enter your age: "))
#if = Do some code only IF some condition is True
#     Else do something else
#if age >= 99:
#    print("You're really old, are you sure youre not a vampire?")
#elif age >= 18:
#    print("Eres mayor de edad")
#elif age < 0: #elif = else if, it allows us to check multiple conditions, really a lot of conditions if we want, but we have to be careful with the order of the conditions, because the first condition that is True will be executed and the rest will be ignored.
#    print("¿Eres un viajero del tiempo?")
#else:
#    print("Eres menor de edad")

#Usar triple comilla para comentar varias líneas de código, es una buena práctica para explicar el código o para dejar notas para nosotros mismos o para otros desarrolladores que puedan leer nuestro código en el futuro. Es importante comentar nuestro código para que sea más fácil de entender y mantener.
""" Example 2
service = input("Would you like to listen to music? Y/N:")
if service == "Y" or service == "y": #or = or, it allows us to check multiple conditions, if any of the conditions is True, the code will be executed.
    print("Playing music...")
elif service == "N" or service == "n":
    print("Okay, maybe later.")
else:
    print("Invalid input, please enter Y or N.")
"""

#version para que no se cierre hasta que tengamos una respuesta válida y quitamos la validación de mayúsculas y minúsculas con lower(). I din't know how to do it with a while loop, but I know that we can use a while loop to keep asking for input until we get a valid response. We can use a while loop that runs indefinitely until we get a valid response, and inside the loop we can check for the valid responses and break the loop when we get a valid response. It's amazing man.
"""
while True:
    service = input("Would you like to listen to music? y/n: ").lower()  #lower() = lower case, it converts the input to lower case, so we don't have to check for both upper and lower case.

    if service == "y":
        print("Playing music...")
        break
    elif service == "n":
        print("Okay, maybe later.")
        break
    else:
        print("Invalid input, please enter Y or N.")

#Example 3
print("Verificación de número par.")
NumPar = int(input("Ingresa el número a verificar: "))
if NumPar % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

"""

#Sistema de calificaciones
# I know I could do it with a while loop to keep asking for input until we get a valid response, but I want to keep it simple for now, and just check for the valid responses with if statements. We can always improve the code later.

score = int(input("Enter your score: "))
if score >= 90:
    print("NICE! You got an A!")
elif score >= 70:
    print("You could do better, you got a B.")

elif score < 70:
    print("You got a F, you need to work harder.")
else:
    print("You need to work harder.")