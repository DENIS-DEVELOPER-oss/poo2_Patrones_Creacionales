// Patron de diseno STRATEGY (de comportamiento): define una familia de algoritmos,
// los encapsula uno por uno y los hace intercambiables en tiempo de ejecucion.
// El cliente (Contexto) puede cambiar de algoritmo sin modificar su codigo.

#include <iostream>                       // Libreria estandar de entrada/salida
#include <vector>                         // Libreria para usar vector (arreglo dinamico)
using namespace std;                      // Evita anteponer "std::" en cada uso

// Estrategia base: define la interfaz comun
class Estrategia {                        // Clase abstracta que representa "una forma de ordenar"
public:
    virtual void ordenar(vector<int>& datos) = 0;  // Metodo virtual puro: cada estrategia concreta debe implementarlo
};

// Estrategia concreta 1: ordenamiento burbuja
class Burbuja : public Estrategia {       // Hereda de Estrategia: implementa el algoritmo de burbuja
public:
    void ordenar(vector<int>& datos) override {       // Sobrescribe el metodo ordenar
        cout << "Usando ordenamiento BURBUJA\n";      // Avisa que algoritmo se esta usando
        int n = datos.size();                         // Guarda el tamano del vector
        for (int i = 0; i < n - 1; i++)               // Bucle externo: hace n-1 pasadas
            for (int j = 0; j < n - i - 1; j++)       // Bucle interno: compara pares de elementos
                if (datos[j] > datos[j + 1])          // Si estan en el orden incorrecto...
                    swap(datos[j], datos[j + 1]);     // ...los intercambia
    }
};

// Estrategia concreta 2: quicksort
class QuickSort : public Estrategia {     // Hereda de Estrategia: implementa quicksort
    void quicksort(vector<int>& datos, int inicio, int fin) {  // Funcion recursiva auxiliar (privada)
        if (inicio < fin) {                           // Caso base: si el rango tiene mas de un elemento
            int pivote = datos[fin];                  // Elige el ultimo como pivote
            int i = inicio - 1;                       // Indice del menor; arranca antes del inicio
            for (int j = inicio; j < fin; j++)        // Recorre el rango (sin incluir el pivote)
                if (datos[j] <= pivote)               // Si el elemento es menor o igual al pivote...
                    swap(datos[++i], datos[j]);       // ...lo mueve a la zona "menor" e incrementa i
            swap(datos[i + 1], datos[fin]);           // Coloca el pivote en su posicion final
            int p = i + 1;                            // Posicion final del pivote
            quicksort(datos, inicio, p - 1);          // Ordena recursivamente la parte izquierda
            quicksort(datos, p + 1, fin);             // Ordena recursivamente la parte derecha
        }
    }
public:
    void ordenar(vector<int>& datos) override {       // Sobrescribe ordenar como punto de entrada publico
        cout << "Usando ordenamiento QUICKSORT\n";    // Avisa que algoritmo se esta usando
        quicksort(datos, 0, datos.size() - 1);        // Llama a la funcion recursiva con el rango completo
    }
};

// Contexto: usa una estrategia (intercambiable)
class Contexto {                          // Clase cliente que delega el "como ordenar" a la estrategia actual
    Estrategia* estrategia;               // Puntero a la estrategia que se esta usando
public:
    Contexto(Estrategia* e) : estrategia(e) {}            // Constructor: recibe la estrategia inicial
    void setEstrategia(Estrategia* e) { estrategia = e; } // Permite cambiar la estrategia en tiempo de ejecucion
    void ejecutar(vector<int>& datos) { estrategia->ordenar(datos); }  // Delega el trabajo a la estrategia actual
};

void imprimir(const vector<int>& v) {     // Funcion utilitaria para imprimir un vector
    for (int n : v) cout << n << " ";     // Recorre cada elemento y lo imprime separado por espacios
    cout << endl;                         // Salto de linea al final
}

int main() {                              // Funcion principal
    vector<int> datos1 = {5, 2, 9, 1, 7, 3};  // Primer arreglo de prueba
    vector<int> datos2 = {8, 4, 6, 2, 1, 9};  // Segundo arreglo de prueba

    Burbuja b;                            // Instancia la estrategia Burbuja
    QuickSort q;                          // Instancia la estrategia QuickSort
    Contexto ctx(&b);                     // Crea el contexto con Burbuja como estrategia inicial

    cout << "Datos originales 1: ";       // Imprime etiqueta
    imprimir(datos1);                     // Muestra datos1 antes de ordenar
    ctx.ejecutar(datos1);                 // Ordena datos1 usando Burbuja
    cout << "Resultado: ";                // Imprime etiqueta
    imprimir(datos1);                     // Muestra datos1 ya ordenado

    cout << "\nDatos originales 2: ";     // Imprime etiqueta con salto de linea
    imprimir(datos2);                     // Muestra datos2 antes de ordenar
    ctx.setEstrategia(&q);                // Cambia la estrategia a QuickSort en caliente
    ctx.ejecutar(datos2);                 // Ordena datos2 usando QuickSort
    cout << "Resultado: ";                // Imprime etiqueta
    imprimir(datos2);                     // Muestra datos2 ya ordenado
}
