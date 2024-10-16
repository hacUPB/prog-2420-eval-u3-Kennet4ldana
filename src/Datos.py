# menú principal
def menu():
    print("1. Crear vuelo")
    print("2. Mostrar vuelos")
    print("3. Mostrar asientos")
    print("4. Reservar asientos")
    print("5. Cancelar reserva")
    print("6. Salir")


# función para crear vuelo
def crear_vuelo(origen,destino,numero):
    vuelo = {
        "origen": origen,
        "destino": destino,
        "asientos": crear_matriz(27,4),
        "pasajeros": [],
        "numero": numero
    }
    vuelos.append(vuelo)

# crea una matriz para ubicar los puestos
def crear_matriz(filas,puestos_por_fila):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(puestos_por_fila):
            fila.append('*')
        matriz.append(fila)
    return matriz

# mostramos todos los vuelos
def mostrar_vuelos(vuelos):
    contador = 0
    print("Id" +".\tOrigen"+"\tDestino\tOcupación")
    for vuelo in vuelos:
        print(str(contador) +".\t"+vuelo['origen']+"\t"+vuelo["destino"]+"\t"+str(calcular_ocupacion(vuelo))+"%")
        contador = contador + 1

# calcula la ocupación del vuelo
def calcular_ocupacion(vuelo):
    return len(vuelo['pasajeros']) / (27 * 4) * 100 

def reservar_asiento(vuelo,nombre_pasajero,fila,columna):
    pasajero = {
        "nombre" : nombre_pasajero,
        "fila": fila,
        "columna": columna  
    }
    if silla_ocupada(vuelo,fila,columna):
        print("La silla esta ocupada, no se puede añadir pasajero.")
        return
    else:
        vuelos[vuelo]['pasajeros'].append(pasajero)
        vuelos[vuelo]['asientos'][fila][columna] = 'x'
        print(vuelos[vuelo]['asientos'][fila][columna])
        print("Pasajero añadido exitosamente.")

# función que otorga un booleano si la silla está ocupada
# '*' significa silla vacía
# 'x' significa silla ocupada
def silla_ocupada(vuelo,fila,columna):
    if vuelos[vuelo]['asientos'][fila][columna] != '*':
        return True
    else:
        return False

# función para seleccionar vuelo entre los disponibles
def seleccionar_vuelo():
    mostrar_vuelos(vuelos)
    id = int(input("Selecciona el Id del vuelo: "))
    return id

# función para cancelar una reserva
def cancelar_reserva(vuelo,fila,columna):
    if silla_ocupada(vuelo,fila,columna):
        vuelos[vuelo]['asientos'][fila][columna] = "*"
        for pasajero in vuelos[vuelo]['pasajeros']:
            if pasajero['fila'] == fila and pasajero['columna'] == columna:
                vuelos[vuelo]['pasajeros'].remove(pasajero)
    else:
        print("Este asiento no está ocupado.")

# funcion para imprimir puestos
def imprimir_asientos(asientos):
    # imprimir en la primera fila los puestos
    
    for fila in range(len(asientos[0])):
        print("\t" + str(fila),end="\t")
    print()   
  
    for fila in range(len(asientos)):
        print("" + str(fila), end="")
        for columna in range(len(asientos[0])):
            print("\t"+asientos[fila][columna],end = "\t")
        print("")


# estructura de datos con los vuelos
vuelos = []


# opción seleccionada
opt = 0
while opt != 6:
    menu()
    opt = int(input("Selecciona una opción de las anteriores: "))
    if opt == 1:
        origen = input("Ingresa el origen: ")
        destino = input("Ingresa el destino: ")
        numero = input("Ingresa el número del vuelo: ")
        crear_vuelo(origen,destino,numero)
        print("*** Vuelo añadido exitosamente***")
    if opt == 2:
        mostrar_vuelos(vuelos)
    if opt == 3:
        vuelo = seleccionar_vuelo()
        imprimir_asientos(vuelos[vuelo]['asientos'])
    if opt == 4:
        vuelo = seleccionar_vuelo()
        nombre_pasajero = input("Ingrese el nombre del pasajero: ")
        fila = int(input("Ingrese una fila entre 0 y 26:"))
        columna = int(input("Ingrese una columna entre 0 y 3:"))
        reservar_asiento(vuelo,nombre_pasajero,fila,columna)
    if opt == 5:
        vuelo = seleccionar_vuelo()
        fila = int(input("Ingrese una fila entre 0 y 26:"))
        columna = int(input("Ingrese una columna entre 0 y 3:"))
        cancelar_reserva(vuelo,fila,columna)

