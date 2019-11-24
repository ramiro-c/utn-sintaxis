from tadFarmacia import *
from tadMedicamento import *
from tadFecha import *

def pedirDatos():
    ''' Pide todos los datos que se necesitan para cargar un medicamento 
    y luego los retorna '''
    nom = input('Ingrese el nombre: ')
    drog = input('Ingrese la droga: ')
    OS = input('Ingrese la obra social: ')
    plan = input('Ingrese el plan: ')
    impor = pedirImporte()
    fecha = pedirFecha()
    hora = pedirHora()

    return nom,drog,OS,plan,impor,fecha,hora

def pedirImporte():
    ''' Pide el importe hasta que se ingrese un valor correcto
    y luego lo retorna '''
    while True:
        try:
            impor = float(input('Ingrese el importe en numeros: '))
            return impor        
        except:
            print('Importe incorrecto, intente otra vez.')

def pedirFecha():
    ''' Pide una fecha hasta que se ingrese un valor correcto
    y luego lo retorna '''
    while True:
        fecha = input('Ingrese la fecha en el formato "dd/mm/aaaa": ')
        valida = validarFecha(fecha)
        if valida:
            return fecha
        print('Fecha incorrecta, intente otra vez.')

def pedirHora():
    ''' Pide la hora hasta que se ingrese un valor correcto
    y luego lo retorna '''
    while True:
        hora = input('Ingrese hora "hh:mm:ss" (formato de 24 hs): ')
        valida = validarHora(hora)
        if valida:
            return hora
        print('Hora incorrecta, intente otra vez.')

def agregar(listaVenta):    
    ''' Crea un medicamento, lo carga con datos validados
    y luego lo agrega a la lista  '''
    med = crearMed()
    print('\nMedicamento a agregar:')
    nom,drog,OS,plan,impor,fecha,hora = pedirDatos()
    cargarMed(med,nom,drog,OS,plan,impor,fecha,hora)
    agregarMed(listaVenta,med)

def modificarPorNombre(listaVenta):
    ''' Modifica el medicamento elegido con nuevos datos ingresados '''
    if cantMed(listaVenta) != 0:   
        nom = input('Ingrese el nombre del medicamento a modificar: ') 
        listaMed = buscarMedNom(listaVenta,nom)
        
        if cantMed(listaMed) != 0:
            imprimirOpciones(listaMed)
            while True:
                try:
                    opcion = int(input('Elija la opcion que quiere modificar (en numeros): '))
                    valida = validarOpcion(opcion, listaMed)

                    if valida == True:
                        medAModificar = recuperarMed(listaMed,opcion)
                        eliminarMed(listaVenta, medAModificar)
                        print('Cargar los nuevos datos de la venta: ')
                        agregar(listaVenta)
                        print('\nEl medicamento fue modificado con exito.')
                        break
                    else:
                        print('La opcion elegida no es correcta.')
                
                except:
                    print('La opcion elegida no es correcta.')
        else:
            print('No hay medicamentos vendidos con ese nombre.')
    else:
        print('No hay medicamentos vendidos.')

def eliminarPorNombre(listaVenta):
    ''' Elimina el medicamento elegido '''
    if cantMed(listaVenta) != 0:
        
        nom = input('Ingrese el nombre del medicamento a eliminar: ') 
        listaMed = buscarMedNom(listaVenta,nom)
        
        if cantMed(listaMed) != 0:
            imprimirOpciones(listaMed)
            while True:
                try:
                    opcion = int(input('Elija la opcion que quiere eliminar (en numeros): '))
                    valida = validarOpcion(opcion, listaMed)
                    
                    if valida == True:
                        medAEliminar = recuperarMed(listaMed,opcion)
                        eliminarMed(listaVenta, medAEliminar)
                        print('Venta eliminada con exito.')
                        break
                    else:
                        print('La opcion elegida no es correcta.')
                
                except:
                    print('La opcion elegida no es correcta.')
        else:
            print('No hay medicamentos vendidos con ese nombre.')
    else:
        print('No hay medicamentos vendidos.')

def validarOpcion(opcion, listaMed):
    ''' Verifica si la opcion elegida es un valor correcto,
    retorna True si es valida, sino retorna False'''
    if opcion >= 1 and opcion <= cantMed(listaMed):
        return True
    return False

def imprimirOpciones(listaMed):
    ''' Imprime las opciones, con su respectivo numero,
    que se pueden elegir '''
    index = 0
    for med in range(0,cantMed(listaMed)):
        print('----------')
        print('Opcion: ',index+1)
        imprimirMedicamento(listaMed[med])
        index += 1

def descuento(listaVenta):
    ''' Le aplica el descuento a los medicamentos de la lista
    que cumplan esa condicion '''
    if cantMed(listaVenta) != 0:
        plan = input('Ingrese el plan de los medicamentos a los que le quiera aplicar el descuento: ')
        plan = plan.lower()
        modificarImporte(listaVenta,plan)
    else:
        print('No hay medicamentos vendidos.')

def modificarImporte(listaVenta,plan):
    ''' Modifica el importe de los medicamentos que sean del plan indicado '''
    contador = 0
    for medicamento in range(0,cantMed(listaVenta)):
        if verPlan(listaVenta[medicamento]) == plan:
            imprimirMedicamento(listaVenta[medicamento])                
            importe = verImp(listaVenta[medicamento])-verImp(listaVenta[medicamento])*0.2
            print('Importe nuevo: ',importe)			    
            modImp(listaVenta[medicamento],importe)
            contador+=1
    if contador == 0:
        print('No existen ventas de medicamentos con ese plan.')
    else:
        print('Importe/s modificado/s con exito.')

def eliminarPorDroga(listaVenta):
    ''' Elimina un medicamento de la lista con la droga indicada '''
    if cantMed(listaVenta)!=0:
        drog = input('Ingrese la droga de los medicamentos a eliminar: ')
        drog = drog.lower()
        contador = 0
        for medicamento in range(0,cantMed(listaVenta)):
            if verDroga(listaVenta[medicamento]) == drog:               
                eliminarMed(listaVenta,listaVenta[medicamento])
                contador+=1
        if contador == 0:
            print('No existen ventas de medicamentos con esa droga.')
        else:
            print('Venta/s eliminada/s con exito.')
    else:
        print('No hay medicamentos vendidos.')

def generarListado(listaVenta):
    ''' Imprime todos los medicamentos de la lista
    con la obra social deseada '''
    if cantMed(listaVenta) != 0:
        os = input('Ingrese la obra social de los medicamentos a listar: ')
        os = os.lower()
        contador = 0
        for medicamento in range(0,cantMed(listaVenta)):
            if verOS(listaVenta[medicamento]) == os:               
                print('\n')
                imprimirMedicamento(listaVenta[medicamento])
                contador+=1
        if contador == 0:
            print('No existen ventas de medicamentos con esa obra social.')
    else:
        print('No hay medicamentos vendidos.')
        
def listadoPorHora(listaVenta):
    ''' Imprime todos los medicamentos vendidos en la fecha 
    y hasta la hora que se le indiquen '''
    if cantMed(listaVenta) != 0:
        fecha = pedirFecha()
        # Para convertirla al mismo formato: Mes dia, ANIO      
        fecha = cargarFecha(fecha)       
        hora = pedirHora()
        contador = 0
        for medicamento in range(0,cantMed(listaVenta)):            
            if verHora(listaVenta[medicamento]) <= hora and verFecha(listaVenta[medicamento]) == fecha:
                print('\nMedicamento: ',contador+1)
                imprimirMedicamento(listaVenta[medicamento])
                contador += 1
        if contador == 0:
            print('\nNo hubo medicamentos vendidos en esa fecha hasta la hora indicada.')
    else:
        print('No hay medicamentos vendidos.')

def salir():
    ''' Verifica que el usuario de verdad quiera salir,
    retorna True si se verifica, en caso contrario retorna False'''
    salir = input('Seguro que quiere salir? Si/No: ')
    salir = salir.lower()
    
    if salir == 'si':
        print('Finalizando programa...')
        return True
    return False

def main():
    ''' Funcion principal, imprime el menu y permite acceder a las opciones '''
    listaVenta = crearListaMed()
    while True:
        res = input('''        
                    MENU
                    
        a) Agregar venta de medicamento.
        b) Modificar venta de medicamento por nombre.
        c) Eliminar venta de medicamento por nombre.
        d) Modificar importe con un 20% de descuento a medicamentos
        de un plan determinado.
        e) Eliminar todas las ventas de los medicamentos que contengan
        una droga dada.
        f) Generar un listado de los medicamentos que fueron vendidos
        por una obra social.
        g) Dada una hora, listar la cantidad de los medicamentos
        vendidos hasta esa hora.
        h) Salir
    
    	    Respuesta: ''')
        
        res = res.lower()
        
        if res == 'a':
            agregar(listaVenta)
            print('\nEl medicamento fue vendido con exito.')
        elif res == 'b':
            modificarPorNombre(listaVenta)
        elif res == 'c':
            eliminarPorNombre(listaVenta)
        elif res == 'd':
            descuento(listaVenta)
        elif res == 'e':
            eliminarPorDroga(listaVenta)
        elif res == 'f':
            generarListado(listaVenta)
        elif res == 'g':
            listadoPorHora(listaVenta)
        elif res == 'h':
            sal = salir()
            if sal:
                break
        else:
            print('Opcion incorrecta, intente otra vez.')

main()