from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas=[]
    def __init__(self, _nombre, _edad, _altura, _sexo, _añosPracticando, _golesMarcados, _tarjetasRojas, _piernaHabil):
        Persona.__init__(self, _nombre, _edad, _altura, _sexo)
        Deportista.__init__(self, "Futbol", _añosPracticando)
        self._golesMarcados=_golesMarcados
        self._tarjetasRojas=_tarjetasRojas
        self._piernaHabil=_piernaHabil
        Futbolista.listaFutbolistas.append(self)

    @classmethod
    def getListaFutbolistas(cls):
        return cls.listaFutbolistas

    @classmethod
    def setListaFutbolistas(cls, lista):
        cls.listaFutbolistas=lista

    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados=golesMarcados
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas=tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil=piernaHabil

    def __str__(self):
        return "Mi nombre es "+self.getNombre()+" soy profesional en el deporte "+self.getDeporte()+" Tengo "+str(self.getEdad())+" años de edad y llevo "+str(self.getAñosPracticando())+" años en el deporte"