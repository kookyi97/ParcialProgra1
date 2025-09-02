from gestor_viajes import GestorViajes

def main():
    gestor = GestorViajes()

    print("="*50)
    print("       SISTEMA DE REGISTRO DE VIAJES       ")
    print("="*50)

    while True:
        print("\n--- Nuevo viaje ---")
        ruta = input("Ingrese la ruta (ej: Ruta 29, Cojute - San Salvador): ")
        costo = float(input("Ingrese el costo del viaje ($): "))
        tiempo = int(input("Ingrese el tiempo del viaje (minutos): "))

        gestor.agregar_viaje(ruta, costo, tiempo)

        print("\nViaje agregado con éxito ")
        continuar = input("¿Desea agregar otro viaje? (s/n): ").strip().lower()
        if continuar != "s":
            break

    print("\n" + "="*50)
    print("          LISTADO DE TODOS LOS VIAJES        ")
    print("="*50)
    gestor.mostrar_viajes()

    print("\n" + "="*50)
    print("              RESUMEN SEMANAL               ")
    print("="*50)
    gestor.resumen()
    print("\nGracias por usar el sistema de registro de viajes 🚍")

if __name__ == "__main__":
    main()