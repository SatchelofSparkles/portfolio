#include <iostream>
using namespace std;

int main() {
  int year;
  cout << "Please enter a year, and I'll tell you if it's a leap year or not\n";
  cin >> year;
  cout << "your year is: " << year << "\n";
  if (year < 1752) {
    cout << "Leap Years were only brought in in 1752, so your year is NOT a leap year\n";
  }
  else if ((year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)) {
    cout << "Your year is NOT a leap year\n";
  }
  else {
    cout << "Your year IS a leap year!! So go take a jump ;-)\n";
  }
}