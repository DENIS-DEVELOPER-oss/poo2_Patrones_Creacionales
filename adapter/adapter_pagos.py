# Patron de diseno ADAPTER (estructural): permite que dos interfaces incompatibles
# trabajen juntas. El adaptador "traduce" las llamadas de un lado al otro.

# Sistema de pagos en dolares (clase existente que no se puede modificar)
class PagoDolares:                        # Clase "antigua" que solo sabe procesar pagos en USD
    def pagar(self, monto):               # Metodo original: recibe un monto en dolares
        return f"Pago realizado: ${monto} USD"  # Devuelve un string indicando que se cobro en dolares

# Adaptador: convierte soles a dolares y delega al sistema original
class AdaptadorSoles:                     # Clase nueva que actua como puente entre soles y dolares
    TIPO_CAMBIO = 3.80                    # Constante de clase: 1 USD = 3.80 PEN (tipo de cambio fijo)

    def __init__(self, pago_dolares):     # Constructor: recibe la instancia del sistema de pagos en dolares
        self.pago_dolares = pago_dolares  # Guarda la referencia para delegarle luego el cobro

    def pagar_soles(self, monto_soles):                       # Metodo "adaptado": acepta soles en lugar de dolares
        monto_dolares = round(monto_soles / self.TIPO_CAMBIO, 2)  # Convierte soles a dolares y redondea a 2 decimales
        resultado = self.pago_dolares.pagar(monto_dolares)    # Llama al sistema original usando el monto ya convertido
        return f"S/. {monto_soles} convertidos -> {resultado}"   # Devuelve un mensaje combinado con la conversion

# Uso
pago = PagoDolares()                      # Crea una instancia del sistema antiguo (solo entiende dolares)
adaptador = AdaptadorSoles(pago)          # Envuelve ese sistema con el adaptador para que acepte soles

print(adaptador.pagar_soles(380))         # Cobra 380 soles -> ~100 USD
print(adaptador.pagar_soles(1000))        # Cobra 1000 soles -> ~263.16 USD
print(adaptador.pagar_soles(50))          # Cobra 50 soles -> ~13.16 USD
