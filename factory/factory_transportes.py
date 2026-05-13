# Patron de diseno FACTORY METHOD: una clase fabrica decide que objeto
# concreto crear en funcion de un parametro, ocultando la logica de instanciacion.

class Transporte:                         # Clase base abstracta: define la interfaz comun de todos los transportes
    def entregar(self):                   # Metodo que cada subclase debe implementar
        pass                              # No hace nada aqui; es solo una "promesa" para las subclases

class Camion(Transporte):                 # Camion hereda de Transporte (es un tipo de transporte)
    def entregar(self):                   # Sobrescribe el metodo entregar con el comportamiento propio del camion
        return "Entrega por carretera"    # Devuelve el mensaje correspondiente al camion

class Barco(Transporte):                  # Barco tambien hereda de Transporte
    def entregar(self):                   # Sobrescribe entregar
        return "Entrega por mar"          # Mensaje propio del barco

class Avion(Transporte):                  # Avion como subclase de Transporte
    def entregar(self):                   # Sobrescribe entregar
        return "Entrega por aire"         # Mensaje propio del avion

class Tren(Transporte):                   # Tren como subclase de Transporte
    def entregar(self):                   # Sobrescribe entregar
        return "Entrega por ferrocarril"  # Mensaje propio del tren

class Bicicleta(Transporte):              # Bicicleta como subclase de Transporte
    def entregar(self):                   # Sobrescribe entregar
        return "Entrega urbana en bicicleta"  # Mensaje propio de la bicicleta

class Factory:                            # Clase fabrica: centraliza la creacion de transportes
    @staticmethod                         # Decorador: get_transporte no necesita una instancia de Factory para llamarse
    def get_transporte(tipo):             # Recibe un string y devuelve la instancia correspondiente
        if tipo == "camion": return Camion()      # Si el tipo es "camion", crea y devuelve un Camion
        elif tipo == "barco": return Barco()      # Si es "barco", crea y devuelve un Barco
        elif tipo == "avion": return Avion()      # Si es "avion", crea y devuelve un Avion
        elif tipo == "tren": return Tren()        # Si es "tren", crea y devuelve un Tren
        elif tipo == "bicicleta": return Bicicleta()  # Si es "bicicleta", crea y devuelve una Bicicleta

# Uso del patron: el cliente solo pide "dame un transporte de tipo X", sin saber como se construye
t1 = Factory.get_transporte("camion")     # Pide a la fabrica una instancia de Camion
t2 = Factory.get_transporte("barco")      # Pide una instancia de Barco
t3 = Factory.get_transporte("avion")      # Pide una instancia de Avion
t4 = Factory.get_transporte("tren")       # Pide una instancia de Tren
t5 = Factory.get_transporte("bicicleta")  # Pide una instancia de Bicicleta

print(t1.entregar())                      # Imprime "Entrega por carretera"
print(t2.entregar())                      # Imprime "Entrega por mar"
print(t3.entregar())                      # Imprime "Entrega por aire"
print(t4.entregar())                      # Imprime "Entrega por ferrocarril"
print(t5.entregar())                      # Imprime "Entrega urbana en bicicleta"
