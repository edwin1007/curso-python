
#list: crea una lista
lista = list(['hola', 56, 'salut', 45, True])

print(lista)

#len: devuelve la cantidad de elementos
print(len(lista))

#append: agrega un elemento a la lista.
lista.append(32)
print(lista)

#insert: agrega un elemento a la lista en un pasicion x.
lista.insert(1, 'mundo')
print(lista)

#extend: agrega una lista a la lista.
lista.extend([False, 100])
print(lista)

#pop: elimina un elemento x de la lista.
lista.pop(0)
print(lista)

lista.pop(-1) #elimina el ultimo y asi...
print(lista)

#remove: elimina un elemento que se le indica por su contenido.
lista.remove('mundo')
print(lista)

#clear: eliminar todos los elementos.
lista.clear()
print(lista)

#sort: ordena una lista de forma ascendente. no admite strings
lista_1 = [34, 56, 3, 45, 12, True, False]
lista_1.sort()
print(lista_1)

#reverse: invierte una lista(no ordena). no admite strings
#lista_1.sort(reverse=True)

lista_1.reverse()
print(lista_1)

#index: retorna la posicon donde se encuentra un elemento dado.
#si el elemento no esta, lanza un error
print(lista_1.index(45))


