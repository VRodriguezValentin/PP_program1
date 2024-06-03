from datetime import datetime
import re
import os
import PAQUETE_ESTACIONAMIENTO.archivos as arch
class Vehiculo:
    def __init__(self, tipo: str, patente: str) -> None:
        self.tipo = tipo
        self.patente = patente
        self.hora_ingreso = datetime.now().strftime('%d/%m %H:%M')

    def __str__(self) -> str:
        return(f'Patente: {self.patente}')

    def __len__(self) -> int:
        # Devuelve la cantidad de minutos de diferencia entre hora_ingreso y hora_actual.
        hora_actual = datetime.now().strftime('%d/%m %H:%M')
        hora_ingreso = self.hora_ingreso
        
        formato_fecha_hora = '%d/%m %H:%M'
        hora_actual_datetime = datetime.strptime(hora_actual, formato_fecha_hora)
        hora_ingreso_datetime = datetime.strptime(hora_ingreso, formato_fecha_hora)
        diferencia_tiempo = hora_actual_datetime - hora_ingreso_datetime

        minutos_diferencia = diferencia_tiempo.total_seconds() / 60
        return(minutos_diferencia)

    def valida_patente(patente):
        patron = r'^[A-Za-z]{3}-\d{3}$'
        if re.match(patron, patente):
            return True
        else:
            return False

    def alta_vehiculo(tipo, patente, estacionamiento, estacionamientos):
        if tipo == 'auto':
            for estacionamiento_x in estacionamientos:
                for dicts in estacionamiento_x.vehiculos:
                    if patente in dicts['objeto'].patente:
                        return(f'La patente [{patente}] ya se encuentra registarda.')
            nuevo_vehiculo = Vehiculo(tipo, patente)
            dict_vehiculo = {'objeto': nuevo_vehiculo, 'hora_ingreso': nuevo_vehiculo.hora_ingreso}
            estacionamiento.autos.append(dict_vehiculo)
            estacionamiento.vehiculos.append(dict_vehiculo)
            estacionamiento.cant_parcelas_autos_disponibles -= 1
            mensaje = f'Vehiculo [{patente}] Ingreso [{datetime.now().strftime('%d/%m/%Y %H:%M')}]'
            Vehiculo.log(mensaje)
        else:
            for estacionamiento_x in estacionamientos:
                for dicts in estacionamiento_x.vehiculos:
                    if patente in dicts['objeto'].patente:
                        return(f'La patente [{patente}] ya se encuentra registarda.')
            nuevo_vehiculo = Vehiculo(tipo, patente)
            dict_vehiculo = {'objeto': nuevo_vehiculo, 'hora_ingreso': nuevo_vehiculo.hora_ingreso}
            estacionamiento.motos.append(dict_vehiculo)
            estacionamiento.vehiculos.append(dict_vehiculo)
            estacionamiento.cant_parcelas_motos_disponibles -= 1
            mensaje = f'Vehiculo [{patente}] Ingreso [{datetime.now().strftime('%d/%m/%Y %H:%M')}]'
            Vehiculo.log(mensaje)
        return 'Alta realizada con exito!'

    def baja_vehiculo(estacionamiento, dict_vehiculo):
        vehiculo = dict_vehiculo['objeto']
        patente = vehiculo.patente
        if vehiculo.tipo == 'auto':
            estacionamiento.autos.remove(dict_vehiculo)
            estacionamiento.vehiculos.remove(dict_vehiculo)
            estacionamiento.cant_parcelas_autos_disponibles += 1
            minutos_estacionado = Vehiculo.__len__(vehiculo)
            coste_minutos = estacionamiento.coste_hora_auto / 60
            coste_total = minutos_estacionado * coste_minutos
            mensaje = f'Vehiculo [{patente}] Egreso [{datetime.now().strftime('%d/%m/%Y %H:%M')}]'
            Vehiculo.log(mensaje)
            return coste_total
        else:
            estacionamiento.motos.remove(dict_vehiculo)
            estacionamiento.vehiculos.remove(dict_vehiculo)
            estacionamiento.cant_parcelas_motos_disponibles += 1
            minutos_estacionado = Vehiculo.__len__(vehiculo)
            coste_minutos = estacionamiento.coste_hora_moto / 60
            coste_total = minutos_estacionado * coste_minutos
            mensaje = f'Vehiculo [{patente}] Egreso [{datetime.now().strftime('%d/%m/%Y %H:%M')}]'
            Vehiculo.log(mensaje)
            return coste_total
    def vehiculos_mostrar_todo(estacionamiento, lista):
        lista_data = []
        for e in lista:
            if estacionamiento.nombre == e.nombre:
                os.system('cls')
                i = 1
                for vehiculo in e.vehiculos:
                    datos = (f'Vehiculo {i}: (Patente: {vehiculo['objeto'].patente} - Tipo: {vehiculo['objeto'].tipo})')
                    lista_data.append(datos)
                    i += 1
        return lista_data
    
    def vehiculos_mostrar_patentes(estacionamiento, lista):
        lista_patentes = []
        for e in lista:
            if estacionamiento.nombre == e.nombre:
                os.system('cls')
                i = 1
                for vehiculo in e.vehiculos:
                    dato = vehiculo['objeto'].patente
                    lista_patentes.append(dato)
                    i += 1
        return lista_patentes
    
    def desgloce_patente_letras(patente):
        letras = ''
        for letra in patente:
            if letra.isalpha():
                letras += letra
        return letras
    
    def desgloce_patente_numeros(patente):
        numeros = ''
        for caracter in patente:
            if caracter.isdigit():
                numeros += caracter
        return numeros
    
    def log(mensaje):
        fecha_hora_actual = datetime.now()
        formato = fecha_hora_actual.strftime('%d/%m/%Y %H:%M')
        data = f'{formato} : {mensaje}'
        arch.escribir_txt('log.txt',data,'a')