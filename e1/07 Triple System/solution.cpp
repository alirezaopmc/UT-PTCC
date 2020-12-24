#include <iostream>

using namespace std;

int main() {
    int p, a, b, x;
    cin >> p >> a >> b >> x;

    int ans = p / x;
    ans += (ans / a) * b;

    cout << ans;
}