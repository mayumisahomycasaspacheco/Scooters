import csv

COLUMNAS = ["id_alquiler", "id_scooter", "cliente", "fecha_inicio", "fecha_fin", "tarifa_por_minuto", "pago"]

class Archivador_de_Scooters:
    def __init__(self, ruta_archivo = "alquileres.csv"):
        self.ruta_archivo = ruta_archivo
    
    def guardar_todos(self, scooters):
        registros = []
        for scooter in scooters:
            registro = {
                "id_alquiler": scooter.id_alquiler,
                "id_scooter": scooter.id_scooter,
                "cliente": scooter.cliente,
                "fecha_incio": scooter.fecha_inicio,
                "tarifa_por_minuto": scooter.tarifa_por_minuto,
                "pago": scooter.pago,
            }
            
            registros.append(registro)
            
        with open(self.ruta_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DicWriter(archivo, fieldnames=COLUMNAS)
            escritor.writeheader()
            for registro in registros:
                escritor.writerow(registro)