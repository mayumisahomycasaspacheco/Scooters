from datetime import datetime

FORMATO_FECHA = "%Y-%m-%d %H:%M"


class Scooter:

    def __init__(self, id_alquiler, id_scooter, cliente, fecha_inicio,
                 tarifa_por_minuto, fecha_fin="", pago=0.0):
        self.id_alquiler = id_alquiler
        self.id_scooter = id_scooter
        self.cliente = cliente
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tarifa_por_minuto = tarifa_por_minuto
        self.pago = pago

    def calcular_duracion_minutos(self):
        if not self.fecha_fin:
            return 0.0

        inicio = datetime.strptime(self.fecha_inicio, FORMATO_FECHA)
        fin = datetime.strptime(self.fecha_fin, FORMATO_FECHA)

        diferencia = fin - inicio
        segundos = diferencia.total_seconds()
        minutos = segundos / 60

        if minutos < 0:
            return 0.0

        return minutos