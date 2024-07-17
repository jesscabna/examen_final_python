"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""
alumno = {
    'nombre': 'catalina jeje',
    'edad': 19,
    'curso': 'arte y cultura',
    'promedio': 18
}


def imprimir_registro(alumno):
    print("Registro del alumno:")
    for clave, valor in alumno.items():
        print(f"{clave}: {valor}")


def editar_edad(alumno, nueva_edad):
    alumno['edad'] = nueva_edad


print("primer registro")
imprimir_registro(alumno)

print("\nsegundo registro")
nueva_edad = 22
editar_edad(alumno, nueva_edad)
imprimir_registro(alumno)
