//I don't really know how arrays and vectors work yet so you're gonna have to stick with this one for now!

#include <iostream>
using namespace std;

int Fibonacci(int x)
{
    if (x==0){return 0;}
  
    else if (x==1){return 1;}
  
    else {return Fibonacci(x-1)+Fibonacci(x-2);}
}


int main()
  
{
    int y;
    y = Fibonacci(25);
    cout << y << endl;
    return y;
}
