from .tabla_asignacion import *
class DNI:
    numero_dni = ''

    numero_letras=len(TablaAsignacion.tabla)

    DNI_LENGTH = 8


    def __init__(self, numero_dni):
        DNI.validarDni(numero_dni)
        self.numero_dni = numero_dni

    def validarDni(numero_dni):
        if len(numero_dni) != DNI.DNI_LENGTH:
            raise ValueError("Formato de DNI incorrecto")
         
    def obtenerLetraDni(self):
        modulo = int (self.numero_dni) % self.numero_letras
        assert modulo not in TablaAsignacion.letrasProhibidas
        return TablaAsignacion.extraerLetraDesdeDigito(modulo)

    def dniConLetra(self):
        return self.numero_dni + self.obtenerLetraDni()
    


        