

#promedio de duracion

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#diferencia de duracion.
#calculo de porcentaje dalto_curso vs otros_cursos_min

diferencia_con_min = 100 - dalto_curso * 100 / otros_cursos_min
print(f'El curso Dalto dura un {diferencia_con_min} % menos que los cursos mas rapidos.')

#diferencia de duracion.
#calculo de porcentaje dalto_curso vs otros_cursos_max

diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
print(f'El curso Dalto dura un {diferencia_con_max} % menos que los cursos mas lentos.')

#duracion de crudos.
crudo_promedio = 5
crudo_dalto = 3.5

#calculando el porcentaje de tiempo vacio removido. 
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

print(f'El crudo promedio elimina un {tiempo_vacio_promedio} % de tiempo vacio.')
print(f'Este curso eliminó el {tiempo_vacio_dalto} % de tiempo vacio.')

#si se vieran 10 horas de este curso, a cuanto equivale en horas de los cursos promedios.
ver_10_horas = otros_cursos_promedio *100 // dalto_curso / 10

print(f'Ver 10 horas del curso dalto equivale a ver {ver_10_horas} horas de otros cursos')
