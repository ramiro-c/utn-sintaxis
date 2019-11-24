from tadMedicamento import *

def crearListaMed():
	''' Crea lista de medicamentos '''
	lista = []
	return lista

def agregarMed(lista,med):
	''' Agrega medicamento a la lista '''
	lista.append(med)

def eliminarMed(lista,med):
	''' Elimina medicamento de la lista '''
	lista.remove(med)

def cantMed(lista):
	''' Retorna cantidad de medicamentos en la lista '''
	return len(lista)

def recuperarMed(lista,pos):
	''' Retorna el medicamento de esa posicion '''
	return lista[pos-1]

def buscarMedNom(lista,nom):
    ''' Retorna todos los medicamentos que tienen ese nombre en una lista'''
    listaMed = []
    nom = nom.lower()
    for medicamento in range(0,cantMed(lista)):
	    if verNom(lista[medicamento]) == nom:
		    listaMed.append(lista[medicamento])
    return listaMed

def imprimirMedicamento(med):
    ''' Imprime todos los campos de un medicamento '''
    print('Nombre: ',verNom(med))
    print('Droga: ',verDroga(med))
    print('Obra social: ',verOS(med))
    print('Plan: ',verPlan(med))
    print('Importe: ',verImp(med))
    print('Fecha: ',verFecha(med))
    print('Hora: ',verHora(med))