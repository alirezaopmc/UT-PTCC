#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    string s;

    for(int i = n; i > 0; i /= 2) {
        s = "01"[i % 2] + s;
    }

    cout << s << endl;
}