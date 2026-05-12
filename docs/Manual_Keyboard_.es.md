



# Teclado

Módulo para realizar diferentes acciones relacionadas con el teclado

*Read this in other languages: [English](Manual_Keyboard_.md), [Português](Manual_Keyboard_.pr.md), [Español](Manual_Keyboard_.es.md)*

![banner](imgs/Banner_Keyboard_.png)
## Como instalar este módulo

Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.




## How to use this module

Select the characters or combination of keys to send.


## Descripción de los comandos

### Enviar Combinaciones

Envía teclas predefinidas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccione la acción|Selecciona una combinación de teclas predefinida|Alt + Tab|

### Repetir Tecla

Envía una tecla y la cantidad de repeticiones
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccione la tecla|Seleccione la tecla que desea enviar|BACKSPACE|
|Repetir|Número de veces a repetir la acción|5|

### Obtener combinación de teclas

Espera hasta que el usuario presione una tecla o combinación y la alamacena en una variable
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Resultado|Asigna el resultado de la ejecución de la tarea a una variable|resultado|

### Enviar tecla

Comando para enviar tecla cuando falle el comando nativo de 'Envia tecla'. Si se desea escribir en mayúscula, la tecla bloq mayús debe estar desactivada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Texto|Texto a enviar|Lorem ipsum|
|Seleccione la tecla|Tecla a enviar|ENTER|
|Tiempo de espera entre caracteres|Cuanto tiempo se debe esperar para escribir cada caracter|1|
