#include <iostream>
#include <limits> //for maths limits
using namespace std;
int main()
{
    double num1, num2;
    char opration;

    cout << "enter a first number";
    cin >> num1;

    cout << "enter a opration";
    cin >> opration;

    cout << "enter a 2nd number";
    cin >> num2;

    double result;

    switch (opration)
    {
    case '+':
        result = num1 + num2;
        break;

    case '-':
        result = num1 - num2;
        break;

    case '*':
        result = num1 * num2;
        break;

    case '/':
        if (num2 == 0)
        {
            cout << "Error: Division by zero!" << endl;
            return 1; // Indicate an error
        }
        else
        {
            result = num1 / num2;
        }
        break;

    default:
        cout << "Error: Invalid operator!" << endl;
        return 1; // Indicate an error
    }
    cout << "result" << " " << result << endl;

    return 0;
}