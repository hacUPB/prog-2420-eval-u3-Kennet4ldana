[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MuElT52l)
# Unidad 3
---
## Documentación del proyecto
Nombre:  Jhon Kennet Aldana Oviedo
ID:  000462009

# LATAM SEAT SELECTION SYSTEM.
# Descripción
El problema a resolver gira entorno a las aerolíneas, con el desarollo del programa se entregará una aplicación que permita a las aerolíneas ejercer plena gestión sobre la asignación de los puestos para vuelos en distintas rutas.
Esta solución es importante porque aborda una necesidad esencial para todas las aerolíneas de transporte de pasajeros. Se trata de una función imprescindible porque las aerolíneas deben encargarse de asignar de forma eficiente los asientos de sus pasajeros para evitar problemas con los usuarios y con la autoridad aeronáutica del país.
# Alcance
Programa que le permita a las aerolíneas realizar reservas en los asientos para los vuelos, así como cancelarlas, mostrarlas y un submodúlo para crear vuelos y mostrarlos.
# Estructuras de datos utilizadas
Utilizaré listas para almacenar diccionarios, estos diccionarios contendran la información del vuelo y la forma en la que se organizan los asientos. Para la gestión de asientos utilizaré una matriz de tamaño fijo 27 * 4, asumiendo que las aeronaves con las que opera la aerolínea son de tamaño pequeño.
Los pasajeros los implementaré como una lista de diccionarios que irá dentro de los vuelos. De esta forma esta combinación de estructuras de control me permitirá tener control total sobre la asignación de los puestos.
# Pseudocódigo
opt = 0
Imprimir menu
Mientras opt != 6: 
    Si opcion == 1:
            Pedir origen al usuario
            Pedir destino al usuario
            Pedir numero_de_vuelo al usuario
            Llamar a crear_vuelo(origen, destino, numero_de_vuelo)
            Imprimir *** Vuelo añadido exitosamente***
            
        Si opcion == 2:
            Llamar a mostrar_vuelos(vuelos)
            
        Si opcion == 3:
            Llamar a seleccionar_vuelo()
            Llamar a imprimir_asientos(asientos del vuelo seleccionado)

        Si opcion == 4:
            Llamar a seleccionar_vuelo()
            Pedir nombre del pasajero
            Pedir fila y columna
            Llamar a reservar_asiento(vuelo, nombre_pasajero, fila, columna)

        Si opcion == 5:
            Llamar a seleccionar_vuelo()
            Pedir fila y columna
            Llamar a cancelar_reserva(vuelo, fila, columna)
---
