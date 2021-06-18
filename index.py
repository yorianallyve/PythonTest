def saludar():
    print("Hola")

def __init__():
    print("Hi")

print("Saludo 1")

saludar()


#tupla
nombes_asignados=("Juan", "Dante", "Randy", "Venus")
print(nombes_asignados)
print(nombes_asignados[0])
print(nombes_asignados[2])
print(nombes_asignados[1:3])
print(nombes_asignados[1:2])
print(nombes_asignados[2:])
print(nombes_asignados[:2])
print(nombes_asignados[-1])
print(nombes_asignados[-2])

#Lista
colores_asignados=["Negro", "Café", "Blanc", "Gris"]
print(colores_asignados)
print(colores_asignados[1])
colores_asignados[2] = "Rojo"
print(colores_asignados[2])


#Diccionarios
vehiculos={'vehiculo_uno':123, 'vehiculo_dos':456, 'vehiculo_tres':789, 'vehiculo_cuatro':192}
print(vehiculos['vehiculo_cuatro'])
print(vehiculos)
print(vehiculos['vehiculo_dos'])
del(vehiculos['vehiculo_tres'])
print(vehiculos)
