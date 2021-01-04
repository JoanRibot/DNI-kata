from src.tabla_asignacion import *

def test_extraerLetraDesdeDigito():
    assert TablaAsignacion.extraerLetraDesdeDigito(4)=="G"
    assert TablaAsignacion.extraerLetraDesdeDigito(22)=="E"
    assert TablaAsignacion.extraerLetraDesdeDigito(20)=="C"
    assert TablaAsignacion.extraerLetraDesdeDigito(15)=="S"
    assert TablaAsignacion.extraerLetraDesdeDigito(11)=="B"
