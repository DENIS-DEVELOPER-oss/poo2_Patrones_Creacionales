# Patron de diseno DECORATOR (estructural): permite agregar responsabilidades
# adicionales a una funcion u objeto sin modificar su codigo original.
# En Python se implementa de forma natural con la sintaxis @decorador.

# Decorator: valida que los argumentos sean numeros
def validar_numeros(func):                # Recibe la funcion que se quiere "decorar" (envolver)
    def envoltura(*args):                 # Funcion interna que reemplazara a la original; acepta cualquier cantidad de argumentos
        for arg in args:                  # Recorre cada argumento recibido
            if not isinstance(arg, (int, float)):     # Si alguno NO es int ni float...
                return f"Error: '{arg}' no es un numero valido"  # ...corta y devuelve un mensaje de error
        return func(*args)                # Si todos eran numeros, ejecuta la funcion original con sus argumentos
    return envoltura                      # Devuelve la nueva funcion envoltura (que reemplaza a la original)

# Decorator: valida que no haya division entre cero
def validar_no_cero(func):                # Decorador especifico para evitar division por cero
    def envoltura(a, b):                  # Aqui sabemos que la funcion recibe exactamente 2 argumentos
        if b == 0:                        # Si el divisor es cero...
            return "Error: no se puede dividir entre cero"   # ...corta y avisa
        return func(a, b)                 # Si no, llama a la funcion original
    return envoltura                      # Devuelve la version envuelta

@validar_numeros                          # Aplica el decorador validar_numeros a la funcion sumar
def sumar(a, b):                          # Funcion original (sin saber que esta siendo envuelta)
    return f"Suma: {a} + {b} = {a + b}"   # Calcula y devuelve la suma formateada

@validar_numeros                          # Aplica validar_numeros a multiplicar
def multiplicar(a, b):                    # Funcion original que multiplica
    return f"Multiplicacion: {a} * {b} = {a * b}"  # Calcula y devuelve el resultado

@validar_numeros                          # Decorador externo: primero valida que sean numeros
@validar_no_cero                          # Decorador interno: luego valida que el divisor no sea cero
def dividir(a, b):                        # Funcion original que divide
    return f"Division: {a} / {b} = {a / b}"  # Calcula y devuelve el resultado

# Pruebas
print(sumar(5, 10))                       # Caso valido: imprime "Suma: 5 + 10 = 15"
print(multiplicar(4, 6))                  # Caso valido: imprime "Multiplicacion: 4 * 6 = 24"
print(dividir(20, 4))                     # Caso valido: imprime "Division: 20 / 4 = 5.0"
print(dividir(10, 0))                     # Division entre cero: el decorador validar_no_cero lo intercepta
print(sumar("hola", 5))                   # Argumento no numerico: validar_numeros lo intercepta y devuelve error
