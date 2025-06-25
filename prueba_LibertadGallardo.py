

# Acá acordamos el stock de entradas para la funcion de "CATS" para el día Viernes y Sábado respectivamente 
stock_func1 = 150
stock_func2 = 180
compradores = {} # Acá creamos una lista para alamcenar los compradores en una sola variable

# Acá creamos el bloque de código para la opcion 1
def comprar_entrada(nombre, funcion): # Acá definimos una función con el nombre comprar_entrada y sus parámetros.
    global stock_func1, stock_func2 # Global para modificar una variable exterior(global)

    if nombre in compradores:
        return "Error. El nombre ya está registrado." # Verifica si el nombre ya está registrado

 # Este bloque permite comprar entradas a la funcion del día viernes, descontando la cantidad al stock inicial. Si queda stock mostrará compra exitosa, sino mostrará no hay entradas.
    if funcion == "1" and stock_func1 > 0:   
        compradores[nombre] = "Cats Día Viernes"
        stock_func1 -= 1       
        return "Compra registrada exitosamente para Cats Día Viernes." 
    elif funcion == "2" and stock_func2 > 0:
        compradores[nombre] = "Cats Día Sábado"
        stock_func2 -= 1
        return "Compra registrada exitosamente para Cats Día Sábado."
    else:
        return "Error. No hay entradas disponibles para esta función."




