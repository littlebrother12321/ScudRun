#include <iostream>
using namespace std;

int main()
{
    float num1;
    float num2;
    float ans;

    cout << "What is the first number?" << endl;
    cin >> num1;
    cout << endl << "What is the second number?" << endl;
    cin >> num2;
    ans = num1 + num2;
    cout << endl << "The answer is: " << ans << endl;

    return 0;
}
