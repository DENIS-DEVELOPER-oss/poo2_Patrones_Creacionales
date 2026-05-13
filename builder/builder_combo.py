# Patron de diseno BUILDER: separa la construccion de un objeto complejo
# de su representacion, permitiendo crear el objeto paso a paso.

class Combo:                              # Define la clase Combo (el "producto" que se va a construir)
    def __init__(self):                   # Constructor: se ejecuta al crear un objeto Combo
        self.hamburguesa = None           # Atributo hamburguesa, inicialmente vacio (None)
        self.bebida = None                # Atributo bebida, inicialmente vacio (None)
        self.papas = None                 # Atributo papas, inicialmente vacio (None)

class Builder:                            # Define la clase Builder (el "constructor" del Combo)
    def __init__(self):                   # Constructor del Builder
        self.combo = Combo()              # Crea internamente un Combo vacio que se ira llenando

    def add_hamburguesa(self, hamburguesa):   # Metodo para agregar la hamburguesa al combo
        self.combo.hamburguesa = hamburguesa  # Asigna el valor recibido al atributo hamburguesa del combo
        return self                           # Devuelve el propio Builder para encadenar llamadas (method chaining)

    def add_bebida(self, bebida):         # Metodo para agregar la bebida al combo
        self.combo.bebida = bebida        # Asigna el valor recibido al atributo bebida del combo
        return self                       # Devuelve self para seguir encadenando

    def add_papas(self, papas):           # Metodo para agregar las papas al combo
        self.combo.papas = papas          # Asigna el valor recibido al atributo papas del combo
        return self                       # Devuelve self para seguir encadenando

    def build(self):                      # Metodo final que entrega el combo ya construido
        return self.combo                 # Retorna el objeto Combo completo

# Uso del patron: se encadenan los metodos add_* y al final build() devuelve el Combo listo
combo = Builder().add_hamburguesa("Hamburguesa doble queso").add_bebida("Coca-Cola grande").add_papas("Papas medianas").build()
print(vars(combo))                        # vars(obj) devuelve el dict de atributos del objeto; aqui imprime el combo armado
