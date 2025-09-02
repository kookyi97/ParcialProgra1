from viaje import Viaje

class GestorViajes:
    def __init__(self):
        self.viajes = []

    def agregar_viaje(self, ruta, costo, tiempo):
        viaje = Viaje(ruta, costo, tiempo)
        self.viajes.append(viaje)

    def mostrar_viajes(self):
        print("\n--- LISTADO DE VIAJES ---")
        for i, viaje in enumerate(self.viajes, start=1):
            print(f"{i}. {viaje}")

    def resumen(self):
        total_costo = sum(v.costo for v in self.viajes)
        total_tiempo = sum(v.tiempo for v in self.viajes)

        print("\n--- RESUMEN SEMANAL ---")
        print(f"Gasto total: ${total_costo:.2f}")
        print(f"Tiempo total: {total_tiempo} minutos")
