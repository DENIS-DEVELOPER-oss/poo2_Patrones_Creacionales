class Transporte:
    def entregar(self):
        pass

class Camion(Transporte):
    def entregar(self):
        return "Entrega por carretera"

class Barco(Transporte):
    def entregar(self):
        return "Entrega por mar"

class Avion(Transporte):
    def entregar(self):
        return "Entrega por aire"

class Tren(Transporte):
    def entregar(self):
        return "Entrega por ferrocarril"

class Bicicleta(Transporte):
    def entregar(self):
        return "Entrega urbana en bicicleta"

class Factory:
    @staticmethod
    def get_transporte(tipo):
        if tipo == "camion": return Camion()
        elif tipo == "barco": return Barco()
        elif tipo == "avion": return Avion()
        elif tipo == "tren": return Tren()
        elif tipo == "bicicleta": return Bicicleta()

t1 = Factory.get_transporte("camion")
t2 = Factory.get_transporte("barco")
t3 = Factory.get_transporte("avion")
t4 = Factory.get_transporte("tren")
t5 = Factory.get_transporte("bicicleta")

print(t1.entregar())
print(t2.entregar())
print(t3.entregar())
print(t4.entregar())
print(t5.entregar())
