"""
crear un funcion que me retorne un diccioonario de la cantidad de vocales que aparecen en un texto pasado por parametro el diccionario debera ser credo por comprension de diccionarios
ejm:
entrada: eucalipto
salida: {e:1,u:1,a:1,i:1,o:1}
"""
def vocales(texto):

    vocales = {'a', 'e', 'i', 'o', 'u'}
    resultado = {v: texto.lower().count(v) for v in vocales}
    return resultado

resultado = vocales("eucalipto")
print(resultado)
