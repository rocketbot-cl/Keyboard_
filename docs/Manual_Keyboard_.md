



# Keyboard

Module to do different actions related to the keyboard

*Read this in other languages: [English](Manual_Keyboard_.md), [Português](Manual_Keyboard_.pr.md), [Español](Manual_Keyboard_.es.md)*

![banner](imgs/Banner_Keyboard_.png)
## How to install this module

To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.

## Como usar este modulo

Selecciona los caracteres o combinaciones de teclas a enviar.



## Description of the commands

### Send Combinations

Send predefined keys
|Parameters|Description|example|
| --- | --- | --- |
|Select the action|Select a predefined key combination|Alt + Tab|

### Repeat Key

Send key and repetitions
|Parameters|Description|example|
| --- | --- | --- |
|Select the key|Select the key you want to send|BACKSPACE|
|Repeat|How many times repeat the action|5|

### Get keys

Wait until the user presses a key or combination and store it in a variable
|Parameters|Description|example|
| --- | --- | --- |
|Result|Assign the result of the task execution to a variable|result|

### Send key

Command to send key, when It failed to send native 'Send key'.If you want to write in uppercase, the caps lock key must be disabled.
|Parameters|Description|example|
| --- | --- | --- |
|Text|Text to send|Lorem ipsum|
|Select the key|Key to send|ENTER|
|Time waits between characters|How much time wait between writing characters|1|
