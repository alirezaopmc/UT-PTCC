#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    // for (int i = 1; i <= n; i++) {
    //     for (int j = 0; j < i; j++)
    //         cout << '*' << " \n"[j == i-1];
    // }

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            cout << '*';
            // cout << "*";
            // Ctrl + /
        }
        cout << '\n'; // endl
    }
}