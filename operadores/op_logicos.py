
#AND

bool_1 = False & False #debe retornar true
bool_2 = False & True #debe retornar true
bool_3 = True & False #debe retornar true
bool_4 = True & True #debe retornar true

#OR
bool_5 = False | False #debe retornar true
bool_6 = False | True #debe retornar true
bool_7 = True | False #debe retornar true
bool_8 = True | True #debe retornar true

#NOT
bool_9 = not False #debe retornar true
bool_10 = not True #debe retornar true

print(bool_1, bool_2, bool_3, bool_4)

print(bool_5, bool_6, bool_7, bool_8)

print(bool_9, bool_10)