#include <iostream>
#include <cstdlib> // for rand and srand funtion
#include <ctime>   // for time
using namespace std;

int main()
{
    srand(time(0));
    int secreatnumber = rand() % 100 + 1; // generates a number between 1 and 100
    cout << "welcome to the number guessing game " << endl;

    int guess;
    int numguesess = 0;

    while (true)
    {
        cout << "enter a guessed number " << endl;
        cin >> guess;
        numguesess++;

        if (guess > secreatnumber)
        {
            cout << "enter a low number  " << endl;
        }
        else if (guess < secreatnumber)
        {
            cout << "enter high number  " << endl;
        }
        else
        {
            cout << "you guessd correct number in " << numguesess << endl;
            break; // exit the loop
        }
    }

    return 0;
}