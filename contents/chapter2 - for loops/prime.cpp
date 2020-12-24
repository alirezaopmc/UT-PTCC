#include <iostream>
#include <math.h>
// sqrt(x)

using namespace std;

int main()
{
    int n;
    cin >> n;

    // Method 1
    int cnt = 0;
    for(int i = 1; i <= n ; i++) {
        if (n % i == 0) cnt++;
        // if (cnt == 2 && i != n) {
        //     cnt++;
        //     cnt = -1;
        //     i = n + 10;
        //     // break;
        // }

        // 0.0001 waste time for n = 100
        // 100s waste time for n = 1e18 = 10 ** 18
        // (^: stands for xor - exclusive or)
    }

    if (cnt == 2) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
    
    // cout << (cnt == 2 ? "YES" : "NO");


    // Method 2
    if (n == 2) {
        cout << "YES" << endl;
    } else {
        bool flag = true;

        // isPrime(int n)
        for(int i = 2; i < n; i++) {
            if (n % i == 0) {
                i = n;
                flag = false;
                // For function: return false;
            }
        }
        // For function: return true;

        if (flag) cout << "YES\n"; else cout << "NO\n";
    }


    // Method 3
    if (n == 2) {
        cout << "YES\n" << endl;
    } else {
        bool flag = true;

        for(int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                i = n + 1;
                flag = false;
            }
        }

        // Iterate over odd numbers
        // for(int i = 3; i * i <= n; i+=2) {
        //     if (n % i == 0) {
        //         i = n + 1;
        //         flag = false;
        //     }
        // }

        if (flag) cout << "YES\n"; else cout << "NO\n";

    }
}

// Sieve ?? google