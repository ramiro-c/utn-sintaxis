from datetime import datetime,time,date

def validarFecha(fecha):
    ''' Retorna True si se valida que es una fecha correcta,
    en caso contrario devuelve False'''
    try:
        dia,mes,anio = fecha.split('/')
        
        longitudDia = len(dia)
        longitudMes = len(mes)
        longitudAnio = len(anio)
    
        validDia =  longitudDia > 0 and \
                    longitudDia < 3 and \
                    int(dia) < 32 and \
                    int(dia) > 0

        validMes =  longitudMes > 0 and \
                    longitudMes < 3 and \
                    int(mes) < 13 and \
                    int(mes) > 0
        
        hoy = date.today()
        
        if int(anio) == hoy.year:
            validAnio = longitudAnio == 4 and \
                        int(dia) <= hoy.day and \
                        int(mes) <= hoy.month
        else:
            validAnio = longitudAnio == 4 and \
                        int(anio) < hoy.year
            
        if validDia and validMes and validAnio:
            return True
        return False
    except:
        return False

def validarHora(hora):
    ''' Retorna True si se valida que es una hora correcta,
    en caso contrario devuelve False
        El formato de la hora es de 24 hs '''
    try:
        horas,minutos,segundos = hora.split(':')
        horas,minutos,segundos = int(horas),int(minutos),int(segundos)
        
        validHoras = horas<24 and horas>=0
        validMinutos = minutos<60 and minutos>=0
        validSegundos = segundos<60 and segundos>=0
        
        if validHoras and validMinutos and validSegundos:
            return True
        return False
    except:
        return False

def cargarFecha(f):
    ''' Transforma el string fecha a un tipo de dato "date",
    se asume que la fecha ya se valido
        Se guarda la fecha como: "Mes dia, Anio" '''
    dia,mes,anio = f.split('/')
    fecha = date(int(anio),int(mes),int(dia))
    fecha = datetime.strftime(fecha,'%b %d, %Y')
    return fecha

def cargarHora(h):
    ''' Transforma el string hora a un tipo de dato "time",
    se asume que la hora ya se valido'''
    horas,minutos,segundos = h.split(':')
    hora = time(int(horas), int(minutos), int(segundos))
    hora = time.strftime(hora,'%H:%M:%S')
    return hora