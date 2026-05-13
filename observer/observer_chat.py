# Patron de diseno OBSERVER (de comportamiento): define una dependencia uno-a-muchos
# entre objetos: cuando uno (el sujeto) cambia de estado, todos sus observadores
# son notificados automaticamente.

# Observador: usuario que recibe notificaciones
class Usuario:                            # Clase Observador: representa a alguien interesado en los mensajes
    def __init__(self, nombre):           # Constructor: recibe el nombre del usuario
        self.nombre = nombre              # Lo guarda como atributo

    def actualizar(self, mensaje):        # Metodo que sera llamado por el sujeto cuando haya novedad
        print(f"[{self.nombre}] recibio: {mensaje}")  # Imprime el mensaje recibido junto al nombre

# Sujeto: el chat que notifica a sus observadores
class Chat:                               # Clase Sujeto: mantiene la lista de observadores y dispara notificaciones
    def __init__(self, nombre):           # Constructor: recibe el nombre del chat
        self.nombre = nombre              # Guarda el nombre
        self.usuarios = []                # Lista (inicialmente vacia) de observadores suscritos

    def registrar(self, usuario):         # Metodo para suscribir un observador al sujeto
        self.usuarios.append(usuario)     # Lo agrega a la lista de observadores
        print(f">> {usuario.nombre} se unio al chat '{self.nombre}'")  # Mensaje informativo

    def enviar(self, mensaje):                            # Metodo que publica un mensaje en el chat
        print(f"\n--- Nuevo mensaje en '{self.nombre}': {mensaje} ---")  # Encabezado del envio
        for u in self.usuarios:                           # Recorre todos los observadores registrados
            u.actualizar(mensaje)                         # Notifica a cada uno llamando a su metodo actualizar

# Uso
chat = Chat("POO II")                     # Crea un chat (sujeto) llamado "POO II"

ana = Usuario("Ana")                      # Crea un observador llamado Ana
luis = Usuario("Luis")                    # Crea un observador llamado Luis
maria = Usuario("Maria")                  # Crea un observador llamado Maria

chat.registrar(ana)                       # Suscribe a Ana al chat
chat.registrar(luis)                      # Suscribe a Luis al chat
chat.registrar(maria)                     # Suscribe a Maria al chat

chat.enviar("Hola a todos!")              # Publica un mensaje: los 3 observadores lo reciben automaticamente
chat.enviar("Recuerden entregar la tarea")    # Publica otro mensaje: los 3 vuelven a ser notificados
