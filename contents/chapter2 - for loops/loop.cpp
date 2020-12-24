#include <iostream>

using namespace std;

int main()
{
    for(int i = 0, int j = 0; i<10; i += 2, j++, cout << "\n+\n") {
        cout << "--> " << i+2 << endl;
    }
}