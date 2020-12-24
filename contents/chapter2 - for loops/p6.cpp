#include <iostream>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    int copyN = n;
    int copyM = m;

    for(; n > 0 && m > 0;) {
        // Swap
        if (n < m) {
            int temp = n;
            n = m;
            m = temp;
        }
        // n > m

        n = n % m;
    }

    cout << "GCD =" << m << endl;
    cout << "LCM =" << copyN * copyM / m << endl;
}