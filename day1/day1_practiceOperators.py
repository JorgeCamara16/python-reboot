a = 10
b = 5
c = 4

# Arithmetic Operators
suma = a + b
resta = a - b
multiplicacion = a * b #interesting fact: I can use the asterisk to multiply words
#print("Hola" * 3) This will print "HolaHolaHola"
division = a / b
modulo = a % b # Resto de la división
exponente = a ** c # Potencia
division_entera = a // b # División sin decimales

#Comparison Operators, they return a boolean value (True or False)
mayor_que = a > b
menor_que = a < b
mayor_o_igual = a >= b
menor_o_igual = a <= b
igual = a == b
diferente = a != b

#Comparison Operators with strings
string1 = "Hola"
string2 = "Mundo"
comparacion_strings = string1 == string2 # This will return False because "Hola" is not equal to "Mundo"
comparacion_strings2 = string1 != string2 # This will return True because "Hola" is not equal to "Mundo"
#When I use comparison operators with strings, it compares them lexicographically (like in a dictionary)
comparacion_strings3 = "Hola" > "Mundo" # This will return False because "H" comes before "M" in the alphabet
comparacion_strings4 = "Hola" < "Mundo" # This will return True because "H" comes before "M" in the alphabet
#If I want to compare the length of the strings, I can use the len() function
comparacion_strings5 = len(string1) > len(string2) # This will return False because Hola is shorter than Mundo (4 characters vs 5 characters)
comparacion_strings6 = len(string1) == len(string2) # This will return False because Hola is shorter than Mundo (4 characters vs 5 characters)
comparacion_strings7 = len(string1) < len(string2) # This will return True because Hola is shorter than Mundo (4 characters vs 5 characters)

#other case of comparison operators with strings is when we have uppercase and lowercase letters, because in ASCII, uppercase letters come before lowercase letters
comparacion_strings8 = "Hola" > "hola" # This will return False because "H" comes before "h" in the ASCII table
comparacion_strings9 = "Hola" < "hola" # This will return True because "H" comes before "h" in the ASCII table

# Logical Operators
and_operator = (a > b) and (c < b) # This will return False because c is not less than b
or_operator = (a > b) or (c < b) # This will return True because a is greater than b
not_operator = not (a > b) # This will return False because a is greater than b, but the not operator negates it

#print((not(7 != 7) and 6 > 5 ) and ('rozar' < 'rotar' or not ( 3 == 5))) # This will return True.

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

#Test 
prom3num = (a + b + c) / 3
print("Promedio de a, b y c:", prom3num)

