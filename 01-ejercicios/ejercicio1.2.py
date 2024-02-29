
frase = input('decime un frase, y calculo el timpo si tuvieras que decirlo: ')

cantidad_palabras = frase.split(' ')

#muestra la lista de palabras.
print(cantidad_palabras)

#calcula lista de palabras
num_palabras = len(cantidad_palabras)

print(f'Dijiste {num_palabras} palabras y tardarias {num_palabras / 2} en decirlas.')