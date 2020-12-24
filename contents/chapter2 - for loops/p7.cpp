#include <iostream>

using namespace std;

int main()
{
    int start = 10;
    int end = 100;

    for(int i = start; i < end; i++) {
        // Calculate the sum of digits
        int sumOfDigits = 0;
        int copyofI = i;
        for(; copyofI > 0; copyofI /= 10) {// 
            sumOfDigits += copyofI % 10;
        }

        if (i % sumOfDigits == 0) cout << i << endl;
    }
}