#include <iostream>
using namespace std;


int main() {
  const double PI = 3.14159;
  double diameter;
  cout << "Please enter the diameter of the circle and press enter\n";
  cin >> diameter;

  double area;
  area = (PI * diameter * diameter / 4);
  double circumference;
  circumference = (PI * diameter);

  cout << "The area of that circle is: ";
  cout << area;
  cout << "\n";

  cout << "The circumference of the circle is: ";
  cout << circumference;
  cout << "\n";

  //cout << "\n";

  //cout << "Remember that the units for the circumference match the diameter's but area are something squared: centimeters squared or squared inches, something like that.\n";
}

//1) units missing; if a person enters "8 inches", it ignores the string
//2) next stage is to ask how many sf or dp are wanted
//3) would be great to be able to enter any of radius, diameter, circumference or area, and get all others back
//4) further extensions to apply to segments, sectors, donuts
//5) even to present a question (or multiple) to the user and return feedback [this is way beyond the scope of this question]
//6) more relevantly, could generate pi from Liebniz series {(4/1)-(4/3)+(4/5)-(4/7)+...} iterated to a given number of terms