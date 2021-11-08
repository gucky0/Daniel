#include <iostream>
using namespace std;

// declare function (function signature)
void sayHi(string name, int age);

int main()
{
    cout << "Top" << endl;
    sayHi("Daniel", 22);
    sayHi("Hafiz", 24);
    cout << "Bottom" << endl;
    return 0;   
}       

void sayHi(string name, int age)
{
    cout << "Hello " << name << "! you are " << age << "." << endl;
}