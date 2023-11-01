# Automatización de pruebas de la aplicación web Urban Routes

  La aplicación web Urban Routes permite a los usuarios y usuarias solicitar servicios de transporte. En este proyecto se automatizan las prruenas utilizando Selenium y Paython para verificar su funcionamiento.

## Técnicas y tecnologías utilizadas:
  - **Python**: Lenguaje de programación en el que esta escrito el código.
  - **Pytest**: Herramienta que ayuda a realizar las pruebas.
  - **Selenium**: El entorno de pruebas para controlar el navegador usando código.
  - **WebDriver**: Utilizando código se puede controlar el navegador.
  - **Page Object Model (modelo POM)**: Es un patrón de diseño para que los elementos del código esten organizados y sea más fácil el mantenimiento del mismo.

## Archivos
  El proyecto cuenta con dos archivos:
  - **data.py:** Contiene información para abrir la página Urban Routes y las variables constantes para llenar algunos campos.
      - No poner datos personales en las demás variables: *"address_from"*, *"address_to"*, "*phone_number*", "*card_number"*, *"card_code"*.

    
  - **main.py:** Contiene la siguiente información:
      - Se importó la biblioteca *"data"* que almacena las variables constantes para llenar los campos requeridos. También se importaron otras clases de la biblioteca Selenium para interactuar con el navegador: webdriver, Keys, By, expected_conditions, WebDriverWait.
      - La función *"retrieve_phone_code"* devuelve el código de confirmación del teléfono después de haber sido solicitado.
      - En la clase *"UrbanRoutesPage"* se describen los localizadores y los métodos para identificar e interactuar con los elementos de la interfaz de la página de Urban Routes.
      - En la clase *"TestUrbanRoutes"* se definen las pruebas para verificar que las acciones se realicen correctamente. 

## Ejecutar las pruebas
  - Descargar los archivos en una carpeta zip.
  - Corroborar que Python está instalado escribiendo en la terminal el siguiente comando para saber que versión está instalada *python --version*, si se muestra un error se debe instalar Python.
  - En PyCharm.
    - Instalar los paquetes de selenium y pytest.
  - Para ejecutar las pruebas considerar lo siguiente: 
     - En el archivo **data.py**, en la variable *urban_routes_url = "Dentro de las comillas copiar la URL generada sin la barra inclinada (/) al final"*.
     - En el archivo **main.py**, abrir la terminal de PyCharm escribir el comando *pytest main.py* o hacer click en el botón 'Run' (la flecha verde).

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
