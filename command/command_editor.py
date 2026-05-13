# Patron de diseno COMMAND (de comportamiento): encapsula una solicitud como un objeto,
# permitiendo parametrizar, encolar, registrar y deshacer operaciones.

# Receptor: el editor donde se aplican los comandos
class Editor:                             # Clase que conoce el "como" de cada operacion sobre el texto
    def __init__(self):                   # Constructor del editor
        self.texto = ""                   # Inicia el contenido del editor vacio

    def escribir(self, contenido):        # Metodo que agrega texto al final
        self.texto += contenido           # Concatena el nuevo contenido al texto existente

    def borrar(self, n):                  # Metodo que elimina los ultimos n caracteres
        self.texto = self.texto[:-n]      # Slice que se queda con todo menos los ultimos n

# Comando base
class Comando:                            # Interfaz abstracta que define la "forma" de un comando
    def ejecutar(self):                   # Metodo que cada comando concreto implementara para actuar
        pass                              # Vacio: las subclases deben sobrescribirlo
    def deshacer(self):                   # Metodo para revertir lo que hizo el comando
        pass                              # Vacio: opcional, depende de cada comando

# Comando: escribir texto
class EscribirCommand(Comando):           # Comando concreto que sabe escribir en el editor
    def __init__(self, editor, contenido):    # Recibe el editor (receptor) y el texto a escribir
        self.editor = editor              # Guarda referencia al editor
        self.contenido = contenido        # Guarda el contenido a escribir

    def ejecutar(self):                   # Implementacion concreta de ejecutar
        self.editor.escribir(self.contenido)  # Llama al receptor para que realmente escriba
        print(f"Escribir: '{self.contenido}' -> Texto actual: '{self.editor.texto}'")  # Muestra el estado

    def deshacer(self):                   # Implementacion concreta de deshacer
        self.editor.borrar(len(self.contenido))  # Borra exactamente la cantidad de caracteres que escribimos
        print(f"Deshacer escritura -> Texto actual: '{self.editor.texto}'")  # Muestra el estado tras deshacer

# Comando: guardar (simulado)
class GuardarCommand(Comando):            # Comando concreto que "guarda" el documento (simulado)
    def __init__(self, editor):           # Recibe el editor sobre el que actuara
        self.editor = editor              # Guarda referencia al editor

    def ejecutar(self):                   # Implementacion de ejecutar
        print(f"Guardando documento: '{self.editor.texto}'")  # Simula el guardado mostrando el contenido

# Invocador: ejecuta comandos y mantiene historial
class Invocador:                          # Clase que dispara comandos sin saber que hacen por dentro
    def __init__(self):                   # Constructor
        self.historial = []               # Lista que guarda los comandos ya ejecutados (para poder deshacer)

    def ejecutar(self, comando):          # Recibe un comando y lo dispara
        comando.ejecutar()                # Llama al metodo ejecutar del comando recibido
        self.historial.append(comando)    # Lo agrega al historial por si se quiere deshacer luego

    def deshacer(self):                   # Deshace el ultimo comando ejecutado
        if self.historial:                # Solo si hay algo en el historial
            comando = self.historial.pop()    # Saca (y elimina) el ultimo comando de la lista
            comando.deshacer()            # Llama a su metodo deshacer

# Uso
editor = Editor()                         # Crea el receptor (editor vacio)
inv = Invocador()                         # Crea el invocador (gestor de comandos)

inv.ejecutar(EscribirCommand(editor, "Hola "))   # Ejecuta comando: escribir "Hola "
inv.ejecutar(EscribirCommand(editor, "mundo!"))  # Ejecuta comando: escribir "mundo!"
inv.ejecutar(GuardarCommand(editor))             # Ejecuta comando: guardar el documento
inv.deshacer()                                   # Deshace el ultimo (guardar no tiene deshacer, asi que no afecta texto)
inv.deshacer()                                   # Deshace el anterior: quita "mundo!"
