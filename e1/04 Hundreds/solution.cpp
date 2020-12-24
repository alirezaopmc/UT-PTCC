#include <iostream>

using namespace std;

int main() {
    long long n;
    cin >> n;

    int ans = (n / 100) % 10;

    cout << ans << endl;
}