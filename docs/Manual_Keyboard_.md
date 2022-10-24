# Keyboard
  
Module to perform different actions related to the keyboard  

*Read this in other languages: [English](Manual_keyboard_.md), [Portugues](Manual_keyboard_.pr.md), [Español](Manual_keyboard_.es.md).*
  
![banner](imgs/Banner_Keyboard_.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


## How to use this module

Select the characters or combination of keys to send.



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
  
Command to send key, when It failed to send native 'Send key'.If you want to write in uppercase, the caps lock key must be disabled
|Parameters|Description|example|
| --- | --- | --- |
|Text|Text to send|Lorem ipsum|
|Select the key|Key to send|ENTER|
|Time waits between characters|How much time wait between writing characters|1|
