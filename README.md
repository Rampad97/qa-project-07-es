# Automatización de pruebas de la aplicación web Urban Routes

  La aplicación web Urban Routes permite a los usuarios y usuarias solicitar servicios de transporte. En este proyecto se automatizan las prruenas utilizando Selenium y Paython para verificar su funcionamiento.

## Técnicas y tecnologías utilizadas:
  - Python: Lenguaje de programación en el que esta escrito el código.
  - Selenium: El entorno de pruebas para controlar el navegador usando código.
  - Page Object Model (modelo POM): Es un patrón de diseño para que los elementos del código esten organizados y sea más fácil el mantenimiento del mismo.

## Archivos
  El proyecto cuenta con dos archivos:
  - **data.py:**
      Contiene información, variables constantes para llenar algunos campos.
    
  - **main.py:** los localizadores que se utilizan para  en la interfaz de la aplicación.
      Se describen los localizadores los métodos para identificar e interactuar con los elementos de la interfaz de la página de Urban Routes para realizar y se definen las pruebas para verificar que las acciones se ralicen correctamente.

## Ejecutar las pruebas
  - Descargar los archivos en una carpeta zip.
  - Ejecutar las pruebas en PyCharm.
    - Instalar los paquetes de selenium y pytest 

## Pruebas que se deben comprobar
  Las pruebas automatizadas que se deben comprobar para realizar el proceso completo de pedir un taxi:
  1. Configurar la dirección 
  2. Seleccionar la tarifa Comfort
  3. Rellenar el número de teléfono
  4. Agregar una tarjeta de crédito
  5. Escribir un mensaje para el controlador
  6. Pedir una manta y pañuelos
  7. Pedir 2 helados
  8. Aparece el modal para buscar un taxi
