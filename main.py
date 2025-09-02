from gestor_viajes import GestorViajes

# Definición de la clase GestorViajes
class GestorViajes:
    def __init__(self):
        # Lista donde se almacenarán todos los viajes como diccionarios
        self.viajes = []

    def agregar_viaje(self, ruta, costo, tiempo):
        """
        Método para registrar un nuevo viaje.
        Cada viaje se guarda en la lista como un diccionario con:
        - ruta (str)
        - costo (float)
        - tiempo (int)
        """
        self.viajes.append({
            "ruta": ruta,
            "costo": costo,
            "tiempo": tiempo
        })

    def mostrar_viajes(self):
        """
        Muestra en pantalla todos los viajes registrados.
        Si no hay viajes, avisa al usuario.
        """
        if not self.viajes:
            print("No hay viajes registrados.")
            return
        for i, viaje in enumerate(self.viajes, 1):
            print(f"{i}. Ruta: {viaje['ruta']} | "
                  f"Costo: ${viaje['costo']:.2f} | "
                  f"Tiempo: {viaje['tiempo']} min")

    def resumen(self):
        """
        Genera un resumen semanal de los viajes:
        - Número total de viajes
        - Costo total acumulado
        - Tiempo total acumulado
        - Promedio de costo por viaje
        - Promedio de tiempo por viaje
        """
        if not self.viajes:
            print("No hay datos para generar el resumen.")
            return

        # Cálculo de totales
        total_costo = sum(v["costo"] for v in self.viajes)
        total_tiempo = sum(v["tiempo"] for v in self.viajes)

        # Impresión de estadísticas
        print(f"Total de viajes registrados: {len(self.viajes)}")
        print(f"Costo total acumulado: ${total_costo:.2f}")
        print(f"Tiempo total acumulado: {total_tiempo} minutos")
        print(f"Promedio de costo por viaje: ${total_costo / len(self.viajes):.2f}")
        print(f"Promedio de tiempo por viaje: {total_tiempo / len(self.viajes):.2f} min")


# Función principal del programa
def main():
    # Se crea el gestor que almacenará todos los viajes
    gestor = GestorViajes()

    # Encabezado del sistema
    print("="*50)
    print("       SISTEMA DE REGISTRO DE VIAJES       ")
    print("="*50)

    # Bucle principal para registrar viajes
    while True:
        print("\n--- Nuevo viaje ---")
        
        # Solicitar datos al usuario
        ruta = input("Ingrese la ruta (ej: Ruta 29, Cojute - San Salvador): ")
        costo = float(input("Ingrese el costo del viaje ($): "))
        tiempo = int(input("Ingrese el tiempo del viaje (minutos): "))

        # Guardar viaje en el gestor
        gestor.agregar_viaje(ruta, costo, tiempo)

        print("\nViaje agregado con éxito ✅")

        # Preguntar si desea continuar
        continuar = input("¿Desea agregar otro viaje? (s/n): ").strip().lower()
        if continuar != "s":
            break

    # Mostrar todos los viajes ingresados
    print("\n" + "="*50)
    print("          LISTADO DE TODOS LOS VIAJES        ")
    print("="*50)
    gestor.mostrar_viajes()

    # Mostrar el resumen semanal
    print("\n" + "="*50)
    print("              RESUMEN SEMANAL               ")
    print("="*50)
    gestor.resumen()

    # Mensaje de cierre
    print("\nGracias por usar el sistema de registro de viajes 🚍")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
