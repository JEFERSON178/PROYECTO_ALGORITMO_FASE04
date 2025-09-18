# FASE 4 - Eliminación de cursos, uso de listas, funciones y modularización

cursos = []

def mostrar_menu():
    print("\n--- MENÚ DE CURSOS ---")
    print("1. Agregar curso")
    print("2. Mostrar cursos")
    print("3. Eliminar curso")
    print("4. Salir")

def agregar_curso():
    curso = input("Ingrese el nombre del curso: ")
    cursos.append(curso)
    print("Curso agregado con éxito.")

def mostrar_cursos():
    if not cursos:
        print("No hay cursos registrados.")
    else:
        print("\nLista de cursos:")
        for i, curso in enumerate(cursos, 1):
            print(f"{i}. {curso}")

def eliminar_curso():
    mostrar_cursos()
    if cursos:
        try:
            pos = int(input("Ingrese el número del curso a eliminar: "))
            if 1 <= pos <= len(cursos):
                eliminado = cursos.pop(pos - 1)
                print(f"Curso '{eliminado}' eliminado.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Debe ingresar un número válido.")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_curso()
    elif opcion == "2":
        mostrar_cursos()
    elif opcion == "3":
        eliminar_curso()
    elif opcion == "4":
        print("saliendo del programa...")
        break
    else:
        print("Opción invalida, intentelo otra vez .")
