//Work is still left, have to implement DP

#include <iostream>

using namespace std;



//recursive functions
int factorial(int x)
{
    if (x==1){return 1;}
    else if (x==0){return 0;}
    else {return x*factorial(x-1);}
}

int main()
{
    cout << factorial(4) << endl;
    return 0;

}
