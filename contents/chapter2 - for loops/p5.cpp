#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    // int cnt = 0; wrong line
    for(int i = 2; i <= n; i++) {
        if (n % i == 0) {
            int cnt = 0;
            for(int j = 1; j <= i ; j++) {
                if (i % j == 0) cnt++;
            }
            if (cnt == 2) cout << i << endl;
        }
    }
    
}