
#se crea un diccionario (clave: valor)
diccionario = {
    "nombre": 'Xowkpr',
    "apellido": 'Byaztsh',
    "edad": 100000  
}

print(diccionario)

#keys(): se muestran las claves del diccionario. 
#tambien se usa para iterar.
print(diccionario.keys())

#get(): se obtiene el valor de la clave.
print(diccionario.get('nombre'))

#clear(): elimina los elementos del diccionario.
#diccionario.clear()
print(diccionario)

#pop(): elimina un elemento
#diccionario.pop('nombre')
print(diccionario)

diccionario_iterable = diccionario.items()
print(diccionario_iterable)
