from scooter import Scooter
from archivador_de_scooters import Archivador_de_Scooters

archivador = Archivador_de_Scooters()

s1 = Scooter(1, "SC-045", "Juan Perez", "2026-09-28 10:00", 150.0, "2026-09-28 10:45")
s2 = Scooter(2, "SC-012", "Ana Gomez", "2026-09-28 09:15", 100.0)
archivador.guardar_todos([s1, s2])

lista = archivador.obtener_todos()
for s in lista:
    print(s.id_alquiler, s.id_scooter, s.cliente, s.fecha_inicio, s.fecha_fin, s.pago)

print ("Total: ", len(lista))