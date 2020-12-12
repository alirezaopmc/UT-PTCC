#include <iostream>

int a = 0;

using namespace std;

// Prototypes
int sum(int a, int b);
int dif(int a, int b);
void show();

int main()
{ // Scopre Start
    show();
} // End

// type[int, string] name[myFunction] (arguments) { BODY }
int sum(int a, int b)
{
    return a + b;
}

int dif(int a, int b)
{
    return sum(a, -b);
}

void show()
{
    cout << "Hello World" << endl;
    int n, m;
    cin >> n >> m;
    cout << sum(n, m) << endl;
}

// Testcase
// 4
// n m
// a1 a2 .. am
// n m
// a1 a2 .. am
// n m
// a1 a2 .. am
// n m
// a1 a2 .. am

// int main()
// {
//     int t;
//     cin >> t;
//     while(t--)
//     {
//         solve();
//     }
// }

// t--: use t, t = t - 1:
// while(t){t--; BODY }

// --t: t = t - 1, use
// t = t - 1
// while(t) {}