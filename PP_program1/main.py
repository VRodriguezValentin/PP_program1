import os
import PAQUETE_ESTACIONAMIENTO.procesos as ps
import PAQUETE_ESTACIONAMIENTO.menu as m
import PAQUETE_ESTACIONAMIENTO.estacionamiento as est
import PAQUETE_ESTACIONAMIENTO.vehiculos as v
import PAQUETE_ESTACIONAMIENTO.map_filter_reduce_sort as mfrs
import PAQUETE_ESTACIONAMIENTO.archivos as arch



def main():
    #Inicializacion de variables
    opciones = ['0','1','2','3','4','5','6','7','8','9','10']
    opciones_menu = ['Nuevo estacionamiento','Ingreso de vehículo','Egreso de vehículo','Modificar costes por hora de vehiculos','Listar vehículos estacionados','Listar vehículos ordenados por patente','Recaudación total de todos los estacionamientos','Listar vehiculos filtrados por cantidad','Guardar archivo',' Ver historial de ingresos y egresos']
    vector_estacionamientos = []
    leer = arch.leer_json('db_estacionamientos.json')
    for e in leer:
        estacionamiento = est.Estacionamiento(e['nombre'],e['cantidad total parcelas auto'],e['cantidad total parcelas moto'],e['coste auto'],e['coste moto'])
        estacionamiento.cant_parcelas_autos_disponibles = e['cantidad parcelas disponibles auto']
        estacionamiento.cant_parcelas_motos_disponibles = e['cantidad parcelas disponibles moto']
        for vehi in e['vehiculos']:
            vehiculo = v.Vehiculo(vehi['tipo'],vehi['patente'])
            vehiculo.hora_ingreso = vehi['hora_ingreso']
            dict_vehiculo = {'objeto': vehiculo, 'hora_ingreso': vehiculo.hora_ingreso}
            estacionamiento.vehiculos.append(dict_vehiculo)
            if vehi['tipo'] == 'auto':
                estacionamiento.autos.append(dict_vehiculo)
            else:
                estacionamiento.motos.append(dict_vehiculo)
        vector_estacionamientos.append(estacionamiento)
    print(vector_estacionamientos)

    while True:
        opcion = m.menu('MENU ESTACIONAMIENTO',opciones_menu)
        opcion = ps.validacion_lista(opcion, opciones, 'opcion')
        os.system('cls')

        if opcion == '0':
            print('¡Hasta luego!')
            break
        else:
            match opcion:
                case '1':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t\t   Nuevo Estacionamiento\n╚══════════════════════════════════════════════════╝\n')
                    nombre = ps.get_str('Ingrese un nombre para el estacionamiento: ','¡ERROR! El nombre del estacionamiento no es valido.')
                    nombre_mayus = nombre.capitalize()
                    cant_parcelas_autos = ps.get_int('Ingrese la cantidad de parcelas de autos: ','¡ERROR! Cantidad de parcelas invalida.',0)
                    coste_hora_auto = ps.get_float('Ingrese el coste por hora para los autos: ','¡ERROR! Coste invalido.',0)
                    cant_parcelas_motos = ps.get_int('Ingrese la cantidad de parcelas de motos: ','¡ERROR! Cantidad de parcelas invalida.',0)
                    coste_hora_moto = ps.get_float('Ingrese el coste por hora para los motos: ','¡ERROR! Coste invalido.',0)

                    os.system('cls')
                    print(est.Estacionamiento.alta_estacionamiento(nombre_mayus, cant_parcelas_autos, cant_parcelas_motos, coste_hora_auto, coste_hora_moto, vector_estacionamientos))

                case '2':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t    Ingreso de Vehiculo\n╚══════════════════════════════════════════════════╝\n')
                    tipos = ['auto', 'moto']
                    while True:
                        for e in vector_estacionamientos:
                            print(f'nombre: {e.nombre}, parcelas autos disponibles: {e.cant_parcelas_autos_disponibles}/{e.cant_parcelas_autos_total}, costo autos: {e.coste_hora_auto}, parcelas motos disponibles: {e.cant_parcelas_motos_disponibles}/{e.cant_parcelas_motos_total}, coste motos: {e.coste_hora_moto}')
                        estacionamiento_elegido = input('Seleccione un estacionamiento: ')

                        est_valido = False
                        for e in vector_estacionamientos:
                            if estacionamiento_elegido in e.nombre:
                                est_valido = True
                                estacionamiento_validado = e
                                break
                        if est_valido:
                            os.system('cls')
                            patente = input('Ingrese una patente: ')
                            patente_valida = v.Vehiculo.valida_patente(patente)
                            if patente_valida:
                                os.system('cls')
                                tipo = ps.validacion_lista(ps.get_str('Ingrese el tipo de vehiculo: ','¡ERROR! El tipo de vehiculo no es valido.'), tipos, 'tipo')
                                print(v.Vehiculo.alta_vehiculo(tipo,patente,estacionamiento_validado, vector_estacionamientos))
                                break
                            else:
                                os.system('cls')
                                print('¡ERROR! Solo se admite el formato [XXX-NNN] para las patentes')
                                break
                        else:
                            os.system('cls')
                            print('El estacionamiento no es valido')
                            break


                case '3':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n Egreso de Vehiculo\n╚═════════════════════════════════════════════════════╝\n')
                    while True:
                        for e in vector_estacionamientos:
                            print(f'nombre: {e.nombre}, parcelas autos disponibles: {e.cant_parcelas_autos_disponibles}/{e.cant_parcelas_autos_total}, costo autos: {e.coste_hora_auto}, parcelas motos disponibles: {e.cant_parcelas_motos_disponibles}/{e.cant_parcelas_motos_total}, coste motos: {e.coste_hora_moto}')
                        estacionamiento_elegido = input('Seleccione un estacionamiento: ')

                        est_valido = False
                        for e in vector_estacionamientos:
                            if estacionamiento_elegido in e.nombre:
                                est_valido = True
                                estacionamiento_validado = e
                                break
                        if est_valido:
                            for e in vector_estacionamientos:
                                if estacionamiento_elegido == e.nombre:
                                    os.system('cls')
                                    i = 1
                                    for vehiculo in e.vehiculos:
                                        print(f'Vehiculo {i}: (Patente: {vehiculo['objeto'].patente} - Tipo: {vehiculo['objeto'].tipo})')
                                        i += 1
                            if len(estacionamiento_validado.vehiculos) == 0:
                                os.system('cls')
                                print(f'El estacionamiento {estacionamiento_validado.nombre} se encuentra vacio.')
                                break
                            else:
                                patente_egreso = input('Ingrese la patente del vehiculo a egresar: ')
                                patente_egreso_valida = False
                                for dict_vehiculo in estacionamiento_validado.vehiculos:
                                    if patente_egreso in dict_vehiculo['objeto'].patente:
                                        patente_egreso_valida = True
                                        vehiculo_elegido = dict_vehiculo
                                        break
                                if patente_egreso_valida:
                                    reca = estacionamiento_validado.recaudacion
                                    coste_total = v.Vehiculo.baja_vehiculo(estacionamiento_validado, vehiculo_elegido)
                                    reca += coste_total
                                    os.system('cls')
                                    print(f'Baja realizada con exito! - Coste final: {coste_total}')
                                    break
                                else:
                                    os.system('cls')
                                    print('¡ERROR! La patente no es valida.')
                                    break
                        else:
                            os.system('cls')
                            print('El estacionamiento no es valido')
                            break

                case '4':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n Modificar Costes por Hora de Vehiculos\n╚═════════════════════════════════════════════════════╝\n')
                    while True:
                        for e in vector_estacionamientos:
                            print(f'nombre: {e.nombre}, parcelas autos disponibles: {e.cant_parcelas_autos_disponibles}/{e.cant_parcelas_autos_total}, costo autos: {e.coste_hora_auto}, parcelas motos disponibles: {e.cant_parcelas_motos_disponibles}/{e.cant_parcelas_motos_total}, coste motos: {e.coste_hora_moto}')
                        estacionamiento_elegido = input('Seleccione un estacionamiento: ')

                        est_valido = False
                        for e in vector_estacionamientos:
                            if estacionamiento_elegido in e.nombre:
                                est_valido = True
                                estacionamiento_validado = e
                                break
                        if est_valido:
                            os.system('cls')
                            cambiar_coste_auto = ps.validacion_continuar('¿Desea modificar el coste por hora de autos?\n => ')
                            if cambiar_coste_auto:
                                nuevo_coste_auto = ps.get_float('Ingrese el coste por hora para los autos: ','¡ERROR! Coste invalido.',0)
                            else:
                                nuevo_coste_auto = None
                            os.system('cls')
                            cambiar_coste_moto = ps.validacion_continuar('¿Desea modificar el coste por hora de motos?\n => ')
                            if cambiar_coste_moto:
                                nuevo_coste_moto = ps.get_float('Ingrese el coste por hora para los motos: ','¡ERROR! Coste invalido.',0)
                            else:
                                nuevo_coste_moto = None
                            os.system('cls')
                            print(est.Estacionamiento.modificar_costes(estacionamiento_validado, nuevo_coste_auto, nuevo_coste_moto))
                            break

                        else:
                            os.system('cls')
                            print('El estacionamiento no es valido')
                            break
                case '5':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t Vehiculos Estacionados\n╚═════════════════════════════════════════════════════╝\n')
                    rtn = mfrs.my_map(v.Vehiculo.vehiculos_mostrar_todo, vector_estacionamientos)
                    i = 0
                    for data in rtn:
                        nombre_estacionamiento = vector_estacionamientos[i].nombre
                        print(f'{nombre_estacionamiento}: {data}')
                        i+= 1
                    
                case '6':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t Vehiculos Ordenados por Patente(descendente)\n╚═════════════════════════════════════════════════════╝\n')
                    vector_listas_patentes = []
                    for estacionamient in vector_estacionamientos:
                        lista_patentes = v.Vehiculo.vehiculos_mostrar_patentes(estacionamient, vector_estacionamientos)
                        vector_listas_patentes.append(lista_patentes)
                    print(vector_listas_patentes)
                    i = 0
                    for data in vector_listas_patentes:
                        nombre_estacionamiento = vector_estacionamientos[i].nombre
                        rtn = mfrs.my_sort(data, v.Vehiculo.desgloce_patente_letras,v.Vehiculo.desgloce_patente_numeros,True)
                        print(f'{nombre_estacionamiento}: {rtn}')
                        i+= 1
                case '7':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t Recaudacion total\n╚═════════════════════════════════════════════════════╝\n')
                    lista_recaudaciones = []
                    for estacionamiento in vector_estacionamientos:
                        recau = estacionamiento.recaudacion
                        print(f'Recaudacion {estacionamiento.nombre}: {est.Estacionamiento.__len__(estacionamiento)}\n')
                        lista_recaudaciones.append(recau)
                        suma = lambda a,b: a+b
                    resultado = mfrs.my_reduce(suma, lista_recaudaciones)
                    print(f'Total de recaudaciones: {resultado}')
                case '8':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n Filtrar Vehiculos por Minutos Estacionados\n╚═════════════════════════════════════════════════════╝\n')
                    '''
                    vehiculos_filtrados = []
                    for estacionamiento in vector_estacionamientos:
                        lista_vehiculos = estacionamiento.vehiculos
                        filtro = mfrs.my_filter(lambda mins: mins>60, lista_vehiculos)
                        vehiculos_filtrados.append(filtro)
                        print(vehiculos_filtrados)'''

                    '''
                    vector_lista_pat_min = []
                    for estacionamiento in vector_estacionamientos:
                        lista_vehiculos = estacionamiento.vehiculos
                        for dicts in lista_vehiculos:
                            lista_pat_min = []
                            patente = dicts['objeto'].patente
                            minutos_total = v.Vehiculo.__len__(dicts['objeto'])
                            lista_pat_min.append(patente)
                            lista_pat_min.append(minutos_total)
                            vector_lista_pat_min.append(lista_pat_min)
                    print(lista_pat_min)
                    print(vector_lista_pat_min)'''


                    '''
                    dict_vehi_mins = {'patente':'','minutos':0}
                    lista_discts_vm = []
                    #i= 0
                    for estacionamiento in vector_estacionamientos:
                        lista_dict = estacionamiento.vehiculos
                        for dicts in lista_dict:
                                patente_v = dicts['objeto'].patente
                                minutos_total = v.Vehiculo.__len__(dicts['objeto'])
                                dict_vehi_mins['patente'] = patente_v
                                dict_vehi_mins['minutos'] = minutos_total
                                lista_discts_vm.append(dict_vehi_mins)
                                #i += 1
                    print(lista_discts_vm)'''
                    
                case '9':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t Guradar archivo\n╚═════════════════════════════════════════════════════╝\n')

                    estacio_data = []
                    for e in vector_estacionamientos:
                        vehiculos = []
                        autos = []
                        motos = []
                        for i in range(len(e.vehiculos)):
                            vehiculo_info = {'patente': e.vehiculos[i]['objeto'].patente,'tipo': e.vehiculos[i]['objeto'].tipo,'hora_ingreso': e.vehiculos[i]['hora_ingreso']}
                            vehiculos.append(vehiculo_info)

                        for i in range(len(e.autos)):
                            auto_info = {'patente': e.autos[i]['objeto'].patente,'tipo': e.autos[i]['objeto'].tipo,'hora_ingreso': e.autos[i]['hora_ingreso']}
                            autos.append(auto_info)

                        for i in range(len(e.motos)):
                            moto_info = {'patente': e.motos[i]['objeto'].patente,'tipo': e.motos[i]['objeto'].tipo,'hora_ingreso': e.motos[i]['hora_ingreso']}
                            motos.append(moto_info)

                        estacio = {'nombre': e.nombre,'cantidad total parcelas auto': e.cant_parcelas_autos_total,'cantidad total parcelas moto': e.cant_parcelas_motos_total,
                                   'cantidad parcelas disponibles auto': e.cant_parcelas_autos_disponibles,'cantidad parcelas disponibles moto': e.cant_parcelas_motos_disponibles,
                                   'coste auto': e.coste_hora_auto,'coste moto': e.coste_hora_moto,'vehiculos': vehiculos,'autos': autos,'motos': motos,'recaudacion': e.recaudacion}

                        estacio_data.append(estacio)

                        arch.escribir_json('db_estacionamientos.json', estacio_data)
                    print('\n\nArchivo guardado.')
                case '10':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t Historial Estacionamientos\n╚═════════════════════════════════════════════════════╝\n')
                    arch.leer_txt('log.txt')
                case _:
                    print('¡ERROR! La opcion no es valida')
        
        input('Presione ENTER para continuar...')
        os.system('cls')

main()