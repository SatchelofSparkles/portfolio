#include <iostream>
#include <string>
using namespace std;

int main()
{
    string phrase;
    cout << "Please enter a word or phrase and press \"enter\", and I'll tell you if it's a palindrome or not\n";
    getline(cin, phrase);
    cout << "your phrase is: " << phrase << "\n";

    int length1 = phrase.length();

//    cout << length1 << " characters long\n";
    int counter = 0;

    for (int i = 0; i < length1; i++) {
        int backwards = (length1 - (i + 1));
//        cout << phrase[i] << " vs " << phrase[backwards] << "\n";
        if (phrase[i] != phrase[(backwards)]) {
            counter++;
        }
    }
    if (counter == 0) {
        cout << "Yes, \"" << phrase << "\" is a palindome!";
    }
        else
        {
            cout << "nope, \"" << phrase << "\" is not a palindrome";
        }
    }


//note: capitalised letters register as different than lowercase; spaces count; punctuation counts. Development route: (1) define variants of given phrase cast to lower-case and with spaces stripped, then check for palindrome status of both the original phrase (if so, say, "strict palindrome") or of this cleaned phrase ("standard palindrome")