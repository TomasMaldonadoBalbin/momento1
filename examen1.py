# Jinney Lopez Barrera
# Tomas Maldonado 

almacen = {
    
    }  
continuar = True

print("Menu:")
print("1. Llenar")
print("2. Imprimir")
print("3. Eliminar")
print("4. Editar")
print("5. Salir")

while continuar:
    opcion = input("ponga una opción (1,2,3,4,5): ")
    
    if opcion == '1':
        clave = input('¿Qué prenda desea agregar? ')
        valor = input(clave + ' ,agregue su valor: ')
        almacen[clave] = valor
    elif opcion == '2':
        print(almacen)
    elif opcion == '3':
        clave = input('¿Qué parte desea eliminar? ')
        if clave in almacen:
            almacen.pop(clave)
        else:
            print(f"{clave} no se encontró en el diccionario.")
    elif opcion == '4':
        clave = input('¿Qué parte desea editar? ')
        if clave in almacen:
            valor = input(f'Nuevo valor para {clave}: ')
            almacen[clave] = valor
        else:
            print(f"{clave} no esta en el diccionario.")
    elif opcion == '5':
        continuar = False
    else:
        print("Opción no válida. Seleccione una opción del menú.")