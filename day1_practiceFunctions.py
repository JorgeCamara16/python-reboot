# functions = A block of reusable code 
#             place () after the function name to invoke it

#Example
"""
def display_invoice(username, amount, due_date):
    print(f"Hello dear {username}")
    print(f"Your bill of ${amount:.2f} is due {due_date}")

display_invoice("JorgeCamara", 100.589, "01 december") #We have to send the same number of parameters as the function is wainting for
"""

# return = statement used to end a function
#          and send a result back to the caller

#Example easy
"""
def add(x, y):
    r = x + y
    return r

def rest(x, y):
    r = x - y
    return r

def multi(x, y):
    r = x * y
    return r

def div(x, y):
    r = x/y
    return r

print(add(1, 2))
print(rest(1, 2))
print(multi(1, 2))
print(div(1, 2))
"""
#Example harder
"""
#My way
def fullname(firstN, lastN):
    fullN = firstN.capitalize() +" "+ lastN.capitalize()
    return fullN

print(fullname("jorge", "camara"))

#Another way
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("carlos", "vela")

print(fullname)
"""
""" #My way
#función cuadrado de un número
def cuadradonum(x):
    r = x**2
    return r

print(cuadradonum(7))

#Función que calcule promedio de una lista.
Numeros = [5, 10, 15, 20]
def promedioList(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)

print(promedioList(Numeros))
      
#Recommendations
#función cuadrado de un número
def cuadradonum(x):
    return x**2

print(cuadradonum(10))

#Función que calcule promedio de una lista.
Numeros = [5, 10, 15, 20]

def promedioLista(numeros):
    if not numeros:
        return 0
    return sum(numeros)/len(numeros)

print(promedioLista(Numeros))
"""  
  
#Prueba con diccionarios, es una lista de diccionarios

productos = [
    {"nombre": "Laptop", "precio": 15000},
    {"nombre": "Mouse", "precio": 500}
]

def promedio_precios(lista):
    suma = 0
    if not lista:
        return 0
    for p in lista:
        precio=p.get("precio", 0) #Siempre suma algo válido
        suma += precio
    return suma/len(lista)

print(promedio_precios(productos))

#Esta version es una locura, Pythonic en su máxima expresión
def promedio_precios2(productos):
    if not productos:
        return 0

    total = sum(p.get("precio", 0) for p in productos) #Siempre suma algo válido
    return total / len(productos)

print(promedio_precios2(productos))
