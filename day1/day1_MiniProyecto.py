mensaje = input("Cliente: ")

if "hola" in mensaje:
    print("Bot: Hola, ¿en qué puedo ayudarte?")
elif "precio" in mensaje:
    print("Bot: Nuestros productos comienzan desde $10")
elif "comprar" in mensaje:
    print("Bot: Claro, ¿qué producto te interesa?")
else:
    print("Bot: No entendí tu mensaje")
