# Teclado
  
Módulo para realizar diferentes acciones relacionadas al teclado  

*Read this in other languages: [English](Manual_keyboard_.md), [Portugues](Manual_keyboard_.pr.md), [Español](Manual_keyboard_.es.md).*
  
![banner](imgs/Banner_Keyboard_.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  


## Como usar este módulo

Selecciona los caracteres o combinaciones de teclas a enviar.



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
