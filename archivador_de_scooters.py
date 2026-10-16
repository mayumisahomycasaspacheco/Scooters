import csv
import os

from scooter import Scooter

COLUMNAS = ["id_alquiler", "id_scooter", "cliente", "fecha_inicio", "fecha_fin", "tarifa_por_minuto", "pago"]


class Archivador_de_Scooters:

    def __init__(self, ruta_archivo="alquileres.csv"):
        self.ruta_archivo = ruta_archivo

    def guardar_todos(self, scooters):
        registros = []
        for scooter in scooters:
            registro = {
                "id_alquiler": scooter.id_alquiler,
                "id_scooter": scooter.id_scooter,
                "cliente": scooter.cliente,
                "fecha_inicio": scooter.fecha_inicio,
                "fecha_fin": scooter.fecha_fin,
                "tarifa_por_minuto": scooter.tarifa_por_minuto,
                "pago": scooter.pago,
            }
            
            registros.append(registro)

        with open(self.ruta_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS)
            escritor.writeheader()
            for registro in registros:
                escritor.writerow(registro)

    def obtener_todos(self):
        scooters = []

        if not os.path.exists(self.ruta_archivo):
            return scooters

        with open(self.ruta_archivo, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                scooter = Scooter(
                    id_alquiler=int(fila["id_alquiler"]),
                    id_scooter=fila["id_scooter"],
                    cliente=fila["cliente"],
                    fecha_inicio=fila["fecha_inicio"],
                    tarifa_por_minuto=float(fila["tarifa_por_minuto"]),
                    fecha_fin=fila["fecha_fin"],
                    pago=float(fila["pago"]),
                )
                scooters.append(scooter)

        return scooters