// Patron de diseno COMPOSITE (estructural): permite tratar objetos individuales
// (hojas) y composiciones de objetos (compuestos) de forma uniforme,
// formando estructuras de arbol como carpetas y archivos.

#include <iostream>                       // Incluye la libreria de entrada/salida estandar
#include <vector>                         // Incluye vector (arreglo dinamico) para guardar los hijos
#include <string>                         // Incluye la clase string para texto
using namespace std;                      // Evita escribir "std::" en cada uso

// Componente base: define la interfaz comun
class Componente {                        // Clase base abstracta: representa cualquier elemento (archivo o carpeta)
public:                                   // Miembros publicos accesibles desde fuera
    virtual void mostrar(int nivel = 0) = 0;  // Metodo virtual puro: cada subclase debe implementarlo
};

// Hoja: representa un archivo individual
class Archivo : public Componente {       // Archivo hereda de Componente (es una "hoja" del arbol)
    string nombre;                        // Atributo privado: nombre del archivo
public:
    Archivo(string n) : nombre(n) {}      // Constructor: inicializa el nombre con la lista de inicializacion
    void mostrar(int nivel = 0) override {    // Implementacion del metodo mostrar (override = sobrescribe el de la clase base)
        cout << string(nivel * 2, ' ') << "- " << nombre << endl;  // Imprime con indentacion segun nivel
    }
};

// Compuesto: representa una carpeta que contiene archivos u otras carpetas
class Carpeta : public Componente {       // Carpeta tambien hereda de Componente (es un "compuesto")
    string nombre;                        // Nombre de la carpeta
    vector<Componente*> hijos;            // Lista de punteros a sus hijos (pueden ser Archivos u otras Carpetas)
public:
    Carpeta(string n) : nombre(n) {}      // Constructor: inicializa el nombre
    void agregar(Componente* c) { hijos.push_back(c); }   // Agrega un hijo (cualquier Componente) a la carpeta
    void mostrar(int nivel = 0) override {                // Sobrescribe mostrar para imprimir la carpeta y sus hijos
        cout << string(nivel * 2, ' ') << "[" << nombre << "]" << endl;  // Muestra el nombre de la carpeta indentado
        for (auto h : hijos) h->mostrar(nivel + 1);       // Recorre cada hijo y llama a su mostrar con nivel+1
    }
};

int main() {                              // Funcion principal
    Carpeta raiz("Documentos");           // Crea la carpeta raiz llamada "Documentos"
    Archivo a1("informe.pdf");            // Crea un archivo llamado "informe.pdf"
    Archivo a2("foto.jpg");               // Crea un archivo llamado "foto.jpg"

    Carpeta sub("Proyectos");             // Crea una subcarpeta llamada "Proyectos"
    Archivo a3("codigo.cpp");             // Crea un archivo "codigo.cpp" para meter en la subcarpeta
    Archivo a4("readme.txt");             // Crea un archivo "readme.txt" para la subcarpeta

    sub.agregar(&a3);                     // Agrega "codigo.cpp" dentro de "Proyectos"
    sub.agregar(&a4);                     // Agrega "readme.txt" dentro de "Proyectos"

    raiz.agregar(&a1);                    // Agrega "informe.pdf" a la raiz
    raiz.agregar(&a2);                    // Agrega "foto.jpg" a la raiz
    raiz.agregar(&sub);                   // Agrega la carpeta "Proyectos" como hijo de la raiz

    raiz.mostrar();                       // Muestra todo el arbol desde la raiz (la recursion baja por los hijos)
}
