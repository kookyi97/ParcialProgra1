from gestor_viajes import GestorViajes

def main():
    gestor = GestorViajes()

    print("=== SISTEMA DE REGISTRO DE VIAJES ===")
    while True:
        ruta = input("\nIngrese la ruta (ej: Ruta 29, Cojute - San Salvador): ")
        costo = float(input("Ingrese el costo del viaje ($): "))
        tiempo = int(input("Ingrese el tiempo del viaje (minutos): "))

        gestor.agregar_viaje(ruta, costo, tiempo)

        continuar = input("\n¿Desea agregar otro viaje? (s/n): ").lower()
        if continuar != "s":
            break

    gestor.mostrar_viajes()
    gestor.resumen()

if _name_ == "_main_":
    main()