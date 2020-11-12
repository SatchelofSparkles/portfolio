#include <iostream>
using namespace std;


int main() {
  std::srand(time(0));  // needed once per program run
  int Value = std::rand() % 10 + 19;

  cout << "The value starts at: " << Value << "\n";

  while (Value > 5){
  int a;
  cout << "Your turn. Enter a number from 1 - 3 \n";
  cin >> a;

  Value = Value - a;
  cout << "OK, the value is now: " << Value << "\n";

  cout << "My turn. What shall I take off? ... ah, I know... \n";
  int b = std::rand() % 3 + 1;
  Value = Value - b;
  cout << "I took off " << b << " so the value is now " << Value << "\n";  
}
  cout << "boom boom boom. That's the sound of the alarm - the value is " << Value << " and we're into the Endgame";
}