from src.dni import *


def test_validar_dni():
    assert DNI.validarDni("12345678")==None
    assert DNI.validarDni("00000000")==None
    assert DNI.validarDni("12626734")==None

def test_Dni_obtenerLetra():
    assert DNI("59435473").obtenerLetraDni()=="T"
    assert DNI("02832361").obtenerLetraDni()=="A"
    assert DNI("61463879").obtenerLetraDni()=="J"
    assert DNI("28740598").obtenerLetraDni()=="M"
    assert DNI("23840575").obtenerLetraDni()=="V"

def test_DniConLetra():
    assert DNI("77586982").dniConLetra()=="77586982R"
    assert DNI("61581069").dniConLetra()=="61581069H"
    assert DNI("76340335").dniConLetra()=="76340335T"
    assert DNI("32117932").dniConLetra()=="32117932L"
    assert DNI("43175355").dniConLetra()=="43175355P"
