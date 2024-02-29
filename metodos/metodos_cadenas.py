
cadena_1 = 'hola mundo'

cadena_2 = 'SALUT MONDE'

#dir: devuelve la lista de atributos válidos del objeto pasado.
#print(dir(cadena_1))

#upper: devuelve el texto en mayuscula.
print(cadena_1.upper())

#upper: devuelve el texto en minuscula.
print(cadena_2.lower())

#convierte la primera en mayuscula.
print(cadena_1.capitalize())

#find: busca una cadena en otra, retorna la poscion de la primer letra encontrada. 
#si no la cadena no esta, retorna un -1.
print(cadena_1.find('do'))

#index: igual que find, la diferencia es que retorna(excepcion) un error sino encuentra algo. 
print(cadena_1.index('l'))

#isnumeric: retorna true si es un numero, sino false.
print('354df'.isnumeric())

#isalpha: retorna true si son solo letras, sino false. 
print('gsdñ'.isalpha())

#count: retorna la cantidad de veces que encuentre un cadena.
print('ahksñdflsdfabsbi'.count('fab'))

#len: cuneta la cantidad de caracteres
print(len('sdfg4567'))

#starwith: retorna true si una cadena conmieza con una cadena dada, sino restorna false.
print('hola norma eee'.startswith('h'))

#endwith: retorna true si una cadena termina con una cadena dada, sino retorna false.
print('hola norma eee'.endswith('e'))

#replace: reemplaza una cadena dada por otra, si la encuentra en la cadena.
print('Hello horld'.replace('h', 'www'))

#split: separa cadena con la cadena dada, retorna una lista.
print('hola,hello salut'.split(',')) #solo crea dos elemetos en la lista. 

