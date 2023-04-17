class Deportista:
    def __init__(self, _deporte, _añosPracticando):
        self._deporte=_deporte
        self._añosPracticando=_añosPracticando

    def getDeporte(self):
        return self._deporte

    def setDeporte(self, deporte):
        self._deporte=deporte

    def getAñosPracticando(self):
        return self._añosPracticando
    
    def setAñosPracticando(self, añosPracticando):
        self._añosPracticando=añosPracticando

    
    