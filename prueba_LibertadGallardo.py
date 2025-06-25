
# Stocks iniciales
stock_func1 = 150
stock_func2 = 180
compradores = {}

# Comprar entrada
def comprar_entrada(nombre, funcion):
    global stock_func1, stock_func2
    if nombre in compradores:
        return "Error: Nombre ya registrado."
    
    if funcion == "1" and stock_func1 > 0:
        compradores[nombre] = "Viernes"
        stock_func1 -= 1
        return "Compra exitosa para el viernes."
    elif funcion == "2" and stock_func2 > 0:
        compradores[nombre] = "Sábado"
        stock_func2 -= 1
        return "Compra exitosa para el sábado."
    else:
        return "No hay entradas disponibles."

# Cambiar función
def cambiar_funcion(nombre):
    global stock_func1, stock_func2
    if nombre not in compradores:
        return "Error: Comprador no existe."
    
    actual = compradores[nombre]
    if actual == "Viernes" and stock_func2 > 0:
        compradores[nombre] = "Sábado"
        stock_func1 += 1
        stock_func2 -= 1
        return "Cambio hecho al sábado."
    elif actual == "Sábado" and stock_func1 > 0:
        compradores[nombre] = "Viernes"
        stock_func2 += 1
        stock_func1 -= 1
        return "Cambio hecho al viernes."
    else:
        return "No hay entradas en la otra función."

# Mostrar totales
def mostrar_totales():
    print(f"Entradas disponibles: {stock_func1 + stock_func2}")
    print(f"Entradas vendidas: {(150 - stock_func1) + (180 - stock_func2)}")

# Menú principal
def menu():
    while True:
        print("\n--- Teatro CATS ---")
        print("1. Comprar entrada")
        print("2. Cambiar función")
        print("3. Ver totales")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            funcion = input("Función (1=Viernes, 2=Sábado): ")
            print(comprar_entrada(nombre, funcion))
        elif opcion == "2":
            nombre = input("Nombre: ")
            print(cambiar_funcion(nombre))
        elif opcion == "3":
            mostrar_totales()
        elif opcion == "4":
            print("Fin del programa.")
            break
        else:
            print("Opción inválida.")

menu()


