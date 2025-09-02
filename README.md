# ParcialProgra1

Repositorio del parcial 1 de progamación Computacional III

## Nombre de los integrantes

**Mayerlin Yisel Aguilar Cruz**  
**Marleny Jamileth Martinez Méndez**

---



<p align="center">
  <img src="https://auprides.org/assets/imagenes/logos/universidades/UGB.png" alt="UGB" width="200">
</p>

## Descripción del proyecto

# Este proyecto en Python permite registrar los viajes realizados en transporte público durante la semana, mostrando: Detalle de cada viaje (ruta, costo y tiempo), Gasto total semanal, Tiempo total invertido. Se utiliza programación orientada a objetos (POO) y módulos para organizar el código de manera eficiente.

---

## PREGUNTAS

## 1. ¿Qué ventajas tiene en comparación con poner todo el código en un solo archivo o utilizar módulos?

# Respuesta: Separar viaje.py, gestor_viajes.py y main.py hace que cada parte del programa tenga una función específica y sea más fácil de entender. Ademas las clases Viaje y GestorViajes se pueden usar en otros proyectos sin necesidad de copiar todo el código del main.py. Si necesitamos cambiar cómo se calcula el resumen de viajes o agregar un nuevo atributo a Viaje, solo modificamos el módulo correspondiente, Al separar responsabilidades, no repetimos funciones ni estructuras en distintos lugares.

---

## 2. ¿Cómo aplicaron la Programación Orientada a Objetos en su solución? Describan el papel de las clases creadas

# En nuestro sistema usamos POO de la siguiente manera:

- **Clase Viaje:**  
  # Representa un viaje individual. Almacena los datos de ruta, costo y tiempo de cada viaje. También tiene métodos para mostrar su información.

- **Clase GestorViajes:**  
  # Administra una lista de objetos Viaje. Se encarga de:
#   - Agregar viajes a la lista.
#   - Mostrar todos los viajes ordenadamente.
#   - Calcular el gasto total y tiempo total.

# Ventaja de la POO: cada clase tiene responsabilidades claras y los objetos representan entidades del mundo real (viajes y su gestión), haciendo el código más modular, flexible y fácil de ampliar.

---

## 3. ¿De qué manera el uso de GitHub facilitó el trabajo colaborativo en equipo? Den un ejemplo concreto

# Cada integrante puede subir cambios sin sobrescribir el trabajo del otro. Ademas se puede ver quién modificó qué archivo y cuándo.

## Ejemplo concreto:

# - Mi compañera creo los archivos viaje.py y gestor_viajes.py y los subío a GitHub.
# - Yo cree el archivo main.py y luego lo actualize.
# - Yo hice un cambio renombrando o editando partes del código, y después volvi a realizar más ajustes sobre ese mismo archivo.

# Gracias a GitHub, *pudimos trabajar sobre los mismos archivos sin perder cambios*, revisar el historial de ediciones y mantener el proyecto organizado y sincronizado entre los dos.