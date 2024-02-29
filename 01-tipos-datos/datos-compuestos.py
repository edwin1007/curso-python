
#listas

#las listas se pueden modificar
lista = ['cadena', True, 1, 100, 10.2]

#tuplas: no se pueden modificar.
tupla = ('cadena', True, 1, 100, 10.2)

print('lista: ', lista)

print('tupla: ', tupla)

print('de lista: ' + lista[0]) 

print('de tupla: ' + tupla[0])

#conjuntos 
#no se pueden modificar los elementos, se puede redefinir el conjunto 
#no se puede acceder a un indice del conjunto
#si hay un elemento repetido, al imprir el conjunto, no se muestran los elementos repetidos
#se puede iterar en un conjunto
#son datos desordenados
conjunto = {'cadena', True, 1, 100, 10.2}

print('conjunto: ', conjunto)

conjunto = {'cadena', True, 1, 100, 100, 100}

print('conjunto redefinido: ', conjunto)

#diccionarios.
#no tiene orden
#estructura del diccionario: clave : valor

diccionario = {
    'nombre' : 'name',
    'edad' : 12,
    'documento' : 1233444,
    'codigo_estudiante' : 45678
}

print('diccionario: ', diccionario)

print(diccionario['nombre'], diccionario['documento'])