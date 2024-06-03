class Estacionamiento:
    def __init__(self, nombre: str, cant_parcelas_autos: int, cant_parcelas_motos: int, coste_hora_auto: float, coste_hora_moto: float) -> None:
        self.nombre = nombre
        self.cant_parcelas_autos_total = cant_parcelas_autos
        self.cant_parcelas_motos_total = cant_parcelas_motos
        self.cant_parcelas_autos_disponibles = cant_parcelas_autos
        self.cant_parcelas_motos_disponibles = cant_parcelas_motos
        self.coste_hora_auto = coste_hora_auto
        self.coste_hora_moto = coste_hora_moto
        self.vehiculos = []
        self.autos = []
        self.motos = []
        self.recaudacion = 0

    def __str__(self) -> str:
        return(f'Cantidad de motos: {self.cant_parcelas_motos}\nCantidad de autos: {self.cant_parcelas_autos}\nRecaudacion del dia: {self.recaudacion}')

    def __len__(self) -> str:
        cadena_recaudacion = str(self.recaudacion)
        punto = cadena_recaudacion.find('.')
        if punto != -1:
            numeros = cadena_recaudacion[punto+1:]
            cant_numeros = len(numeros)
            if cant_numeros == 1:
                recaudacion_final = cadena_recaudacion + '0'
            elif cant_numeros == 0:
                recaudacion_final = cadena_recaudacion + '00'
            else:
                recaudacion_final = cadena_recaudacion[:punto+3]
        else:
            recaudacion_final = cadena_recaudacion + '.00'
        return recaudacion_final

    def alta_estacionamiento(nombre: str, cant_parcelas_autos: int, cant_parcelas_motos: int, coste_hora_auto:float, coste_hora_moto: float, lista_est: list):
        for est in lista_est:
            if est.nombre == nombre:
                return (f'Ya existe un estacionamiento con el nombre {nombre}')
        nuevo_estacionamiento = Estacionamiento(nombre, cant_parcelas_autos, cant_parcelas_motos, coste_hora_auto, coste_hora_moto)
        lista_est.append(nuevo_estacionamiento)
        return(f'Estacionamiento {nombre} dado de alta!')
    
    def modificar_costes(estacionamiento, coste_auto = None, coste_moto = None):
        cambios = 0
        if coste_auto != None:
            estacionamiento.coste_hora_auto = coste_auto
            cambios += 1
        
        if coste_moto != None:
            estacionamiento.coste_hora_moto = coste_moto
            cambios += 1

        if cambios > 0:
            return 'Modificacion realizada con exito!'
        else:
            return 'No se realizaron modificaciones.'
    