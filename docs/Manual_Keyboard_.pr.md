



# Teclado

Módulo para realizar diferentes ações relacionadas com o teclado

*Read this in other languages: [English](Manual_Keyboard_.md), [Português](Manual_Keyboard_.pr.md), [Español](Manual_Keyboard_.es.md)*

![banner](imgs/Banner_Keyboard_.png)
## Como instalar este módulo

Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.




## Como usar este módulo

Selecione os caracteres ou a combinação de teclas a serem enviados.


## Descrição do comando

### Enviar Combinacoes

Envia teclas predefinidas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Selecione a ação|Selecione uma combinação de teclas predefinida|Alt + Tab|

### Repetir a chave

Enviar uma chave e o número de repetições
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Selecione a chave|Selecione a chave que você deseja enviar|BACKSPACE|
|Repetir|Número de vezes para repetir a ação|5|

### Obter combinação de teclas

Aguarda até que o usuário pressione uma tecla ou combinação e a armazena em uma variável
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Resultado|Atribua o resultado da execução da tarefa a uma variável|resultado|

### Enviar tecla

Comando para enviar tecla quando falhar o comando nativo de 'Enviar tecla'. Se deseja escrever em maiúsculo, a tecla de bloqueio de maiúsculas deve estar desativada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Texto|Texto para enviar|Lorem ipsum|
|Selecione a tecla|Tecla para enviar|ENTER|
|Tempo de espera entre caracteres|Quanto tempo deve esperar para escrever cada caracter|1|
