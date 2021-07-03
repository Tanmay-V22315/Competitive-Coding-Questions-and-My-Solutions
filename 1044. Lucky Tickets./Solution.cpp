//C++ solution, for dat speed!
#include <iostream>
#include <cmath>
#include <string> 
using namespace std;


int sumchecker(int internum, unsigned char numberOfDigits)
{
    int sum = 0;
    for (int i=0; i < numberOfDigits; i++)
    {
        sum = sum + (internum%10);
        internum = internum/10;
    }
    return sum;
}

//------------------------------------------------------------------------------------------------------------------------------------------------------------------//


int main()
{   
    int x;
    cout << "Number of digits: " ;
    cin >> x;
    int counter = 0;
    int *ptr;
    ptr = &counter;



    int Multiplier1 = pow(10,x>>1);
    int Multiplier2 = pow(10,x);


    for (int y = Multiplier1-1; y < Multiplier2; y= y+2)
    {             
        if (sumchecker(y%Multiplier1, x)==sumchecker(y - y%Multiplier1, x))
        {
            *ptr = *ptr +1;     
        }
    }
    cout <<  *ptr*2 << endl;
    return 0;
}
