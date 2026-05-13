// Patron de diseno SINGLETON: garantiza que una clase tenga una unica
// instancia en todo el programa y provee un punto global de acceso a ella.

#include <iostream>                       // Incluye la libreria estandar de entrada/salida (cout, endl)
using namespace std;                      // Permite usar cout, endl, etc. sin escribir "std::" cada vez

class Config {                            // Declaracion de la clase Config (sera nuestro Singleton)
private:                                  // Miembros privados: solo accesibles dentro de la clase
    static Config* instance;              // Puntero estatico que guardara la unica instancia de Config
    Config() {}                           // Constructor privado: impide crear objetos desde fuera con "new Config()"
public:                                   // Miembros publicos: accesibles desde fuera de la clase
    static Config* getInstance() {        // Metodo estatico que devuelve la unica instancia
        if (!instance) instance = new Config();  // Si aun no existe, se crea por primera vez (lazy initialization)
        return instance;                  // Devuelve el puntero a la instancia ya existente
    }
    void showMessage() { cout << "Configuracion global cargada.\n"; }  // Metodo de ejemplo: imprime un mensaje
};
Config* Config::instance = nullptr;       // Definicion del miembro estatico: inicializa el puntero como nullptr (vacio)

int main() {                              // Funcion principal del programa
    Config* obj1 = Config::getInstance(); // Primera llamada: crea la instancia y la guarda en obj1
    Config* obj2 = Config::getInstance(); // Segunda llamada: NO crea otra, devuelve la misma instancia
    Config* obj3 = Config::getInstance(); // Tercera llamada: tambien apunta a la misma instancia

    obj1->showMessage();                  // Llama al metodo showMessage usando el puntero obj1

    cout << "Direccion obj1: " << obj1 << endl;  // Imprime la direccion de memoria de obj1
    cout << "Direccion obj2: " << obj2 << endl;  // Imprime la direccion de obj2 (sera identica a obj1)
    cout << "Direccion obj3: " << obj3 << endl;  // Imprime la direccion de obj3 (tambien identica)
    cout << "Son iguales? " << (obj1 == obj2 && obj2 == obj3) << endl;  // Verifica que los 3 punteros apuntan al mismo objeto (imprime 1 = true)
}
