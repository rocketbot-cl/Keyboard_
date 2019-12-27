# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

from pywinauto.keyboard import send_keys

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")


if module == "sendKey":
    key_ = GetParams('key_')

    if key_:

        if key_ == "win":
            send_keys('{VK_LWIN down}{VK_LWIN up}')

        if key_ == "wind":
            send_keys('{VK_LWIN down}D{VK_LWIN up}')

        if key_ == "winr":
            send_keys('{VK_LWIN down}R{VK_LWIN up}')

        if key_ == "wine":
            send_keys('{VK_LWIN down}E{VK_LWIN up}')

        if key_ == "ctrlc":
            send_keys('^C')

        if key_ == "ctrlv":
            send_keys('^V')

        if key_ == "ctrla":
            send_keys('^A')

        if key_ == "ctrle":
            send_keys('^E')

        if key_ == "ctrlb":
            send_keys('^B')

    else:
        raise Exception ('Debe seleccionar una opcion')









