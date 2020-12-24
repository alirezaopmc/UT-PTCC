#include <iostream>

using namespace std;

int main()
{
    int n = 10;

    int b1 = -1, b2 = -2, b3 = -66;

    for(int i=0; i<n; i++) {
        int p; // grade
        cin >> p;

        if (p > b1) {
            b3 = b2; //assignment - meghdar dehi
            b2 = b1;
            b1 = p;
        } else if (p > b2) {
            b3 = b2;
            b2 = p;
        } else if (p > b3) {
            b3 = p;
        }
    }

    cout << b1 << endl;
    cout << b2 << endl;
    cout << b3 << endl;
}