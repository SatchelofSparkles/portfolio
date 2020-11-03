#include <iostream>
using namespace std;

int main() {

cout << "not shown: Initialise 3 objects (floats)\n";
 float x = 15.1;
 float y = 12.7;
 float z = 41.6;

cout << "not shown: Initialise 3 pointers\n\n";
float *p, *q, *r;

cout << "Assign each pointer to an object\n";
p = &x;
q = &y;
r = &z;

cout << "p = &x\nq = &y\nr = &z\n\n";

cout << "Table:\n       p          *p     x         &x\n" << "       q          *q     y         &y\n" << "       r          *r     z        &z\n\n";

cout << "Inspecting the pointers and objects\n";
cout << p << "   " << *p << "   " << x << "   " << &x <<"\n";
cout << q << "   " << *q << "   " << y << "   " << &y << "\n";
cout << r << "   " << *r << "   " << z << "   " << &z << "\n\n";

cout << "Performing calculations:\nx = x * 2\n*q = 37.5\n*r = y + z\n\n";

x = x * 2;
*q = 37.5;
*r = y + z;

cout << "Inspecting the pointers and objects again\n";
cout << p << "   " << *p << "   " << x << "   " << &x <<"\n";
cout << q << "   " << *q << "   " << y << "   " << &y <<"\n";
cout << r << "   " << *r << "   " << z << "   " << &z <<"\n\n";

}