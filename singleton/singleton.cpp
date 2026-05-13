#include <iostream>
using namespace std;

class Config {
private:
    static Config* instance;
    Config() {}  // Constructor privado
public:
    static Config* getInstance() {
        if (!instance) instance = new Config();
        return instance;
    }
    void showMessage() { cout << "Configuracion global cargada.\n"; }
};
Config* Config::instance = nullptr;

int main() {
    Config* obj1 = Config::getInstance();
    Config* obj2 = Config::getInstance();
    Config* obj3 = Config::getInstance();

    obj1->showMessage();

    cout << "Direccion obj1: " << obj1 << endl;
    cout << "Direccion obj2: " << obj2 << endl;
    cout << "Direccion obj3: " << obj3 << endl;
    cout << "Son iguales? " << (obj1 == obj2 && obj2 == obj3) << endl;
}
