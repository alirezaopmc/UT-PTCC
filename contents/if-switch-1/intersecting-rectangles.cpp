#include <iostream> // cin cout
#include <algorithm> // min max

using namespace std; // std::cout or std::cin

int main()
{
    // Rect 1 => A(Ax, Ay) B(Bx, By)
    int Ax, Ay, Bx, By;
    cin >> Ax >> Ay >> Bx >> By;

    // Rect 2 => C(Cx, Cy) D(Dx, Dy)
    int Cx, Cy, Dx, Dy;
    cin >> Cx >> Cy >> Dx >> Dy;

    // Change Conditions (WLOG)

    if (Ax > Bx) swap(Bx, Ax);
    // {
    //     int temp = Ax;
    //     Ax = Bx;
    //     Bx = Bx;
    // }

    if (Cx > Dx) swap(Dx, Cx);
    if (Ay > By) swap(By, Ay);
    if (Cy > Dy) swap(Dy, Cy);

    // Intervals intersection

    // X Rect 1 & 2
    // [Ax, Bx] - [Cx, Dx]
    // Max(Ax, Cx)
    // Min(Bx, Dx)
    int startX = max(Ax, Cx); // MAX :Starting Points
    int endX = min(Bx, Dx); // MIN :Enging Points
    int lengthX = 0;
    if (startX < endX) lengthX = endX - startX;

    // Y Rect 1 & 2
    // [Ay, By] - [Cy, Dy]
    // Max(Ay, Cy)
    // Min(By, Dy)
    int startY = max(Ay, Cy); // MAX :Starting Points
    int endY = min(By, Dy); // MIN :Enging Points
    int lengthY = 0;
    if (startY < endY) lengthY = endY - startY;

    long long S = 1LL * lengthY * lengthX;
    // For values less than 2B there is no overflow

    cout << S << endl;
}