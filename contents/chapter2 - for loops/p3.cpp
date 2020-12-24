#include <iostream>

using namespace std;

int main()
{
    int start = 1000;
    int end = 10000;

    for(int i = start; i < end; i++) {
        if (i % 13 == 0 && i % 3 != 0 && i % 5 != 0) {
            cout << i << endl;
        }
    }
}