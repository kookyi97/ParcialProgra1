# Importamos la clase Viaje desde el archivo viaje.py
# Esto permite que GestorViajes pueda crear objetos de tipo Viaje
from viaje import Viaje

class GestorViajes:
    def __init__(self):
         # Lista donde se almacenarán los viajes registrados
        self.viajes = []

    def agregar_viaje(self, ruta, costo, tiempo):
        
        viaje = Viaje(ruta, costo, tiempo)
        self.viajes.append(viaje)

    def mostrar_viajes(self):
        print("\n--- LISTADO DE VIAJES ---")
        for i, viaje in enumerate(self.viajes, start=1):
            # Se imprime cada viaje. La representación de viaje
            # dependerá de cómo esté definido __str__ en la clase Viaje.
            print(f"{i}. {viaje}")

    def resumen(self):
        # Se suman los costos de todos los viajes usando comprensión de listas
        total_costo = sum(v.costo for v in self.viajes)
        # Se suman los tiempos de todos los viajes
        total_tiempo = sum(v.tiempo for v in self.viajes)
        # Se muestran los resultados
        print("\n--- RESUMEN SEMANAL ---")
        print(f"Gasto total: ${total_costo:.2f}")
        print(f"Tiempo total: {total_tiempo} minutos")
