#include <iostream>

using namespace std;

int main() {
    int n, m;
    char c;

    cin >> n >> m >> c;

    for(int i=0; i<n; i++) {
        for (int j=0; j<n-i-1; j++) cout << ' ';
        for (int j=0; j<2*i+1; j++)
            if (j != m-1) cout << c; else cout << ' ';
        cout << endl;
    }
}