from tadFecha import *

def crearMed():
	''' Crea un medicamiento vacio '''
	med = ['','','','',0.0,'','']
	return med

def cargarMed(med,nom,drog,os,plan,impor,fecha,hora):
	''' Carga medicamento con los datos, se asume que los datos ya estan validados. '''
	modNom(med,nom)
	modDroga(med,drog)
	modOS(med,os)
	modPlan(med,plan)
	modImp(med,impor)
	modFecha(med,fecha)
	modHora(med,hora)

def verNom(med):
	''' Devuelve el nombre del medicamento '''
	return med[0]

def verDroga(med):
	''' Devuelve la droga del medicamento '''
	return med[1]

def verOS(med):
	''' Devuelve la obra social del medicamento '''
	return med[2]

def verPlan(med):
	''' Devuelve el plan del medicamento '''
	return med[3]

def verImp(med):
	''' Devuelve el importe del medicamento '''
	return med[4]

def verFecha(med):
	''' Devuelve la fecha del medicamento '''
	return med[5]

def verHora(med):
	''' Devuelve la hora del medicamento '''
	return med[6]

def modNom(med,nom):
	''' Modifica el nombre del medicamento '''
	nom = nom.lower()
	med[0] = nom

def modDroga(med,drog):
	''' Modifica la droga del medicamento '''
	drog = drog.lower()
	med[1] = drog

def modOS(med,os):
	''' Modifica la obra social del medicamento '''
	os = os.lower()
	med[2] = os

def modPlan(med,plan):
	''' Modifica el plan del medicamento '''
	plan = plan.lower()
	med[3] = plan

def modImp(med,impor):
	''' Modifica el importe del medicamento '''
	med[4] = impor

def modFecha(med,f):
	''' Modifica la fecha del medicamento '''
	fecha = cargarFecha(f)
	med[5] = fecha

def modHora(med,h):
	''' Modifica la hora del medicamento '''
	hora = cargarHora(h)
	med[6] = hora