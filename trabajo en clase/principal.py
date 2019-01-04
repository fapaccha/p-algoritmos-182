from paquete_archivos.miarchivo import MiArchivo, MiArchivoEscribir
from modelado.modelo import *

m = MiArchivo() # objeto para leer el archivo
m2 = MiArchivoEscribir() # objeto para escribir el archivo

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

lista_equipos=[]

for i in lista:
    e = Equipo(i[0], i[1], i[2], i[3])
    lista_equipos.append(e)


operacion = Operaciones(lista_equipos)

a = input("Si desea ordenar por nombre seleccione N y si desea ordenar por Campeonato seleccione C ")

if a=='N' or a =='n':
	lista_ordenada=operacion.ordenar_nombre()
else:
	lista_ordenada=operacion.ordenar_campeonatos()

for i in lista_ordenada:
	m2.agregar_informacion(i)
	print(i)


m.cerrar_archivo()
m2.cerrar_archivo()