#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    float sum1 = 0;
    float sum2 = 0;
    for(int i = 1; i < n; i += 2) {
        float element = (float) (i * (i+1)) / (i + i + 1);
        sum1 += element;
    }

    for(int i = 2; i <= n; i += 2) {
        float element = (float) (i * (i-1)) / (i + i - 1);
        sum2 += element;
    }

    printf("%.12f\n", sum1);
    printf("%.12f\n", sum2);
    // 12 is alot, use 6 instead
}