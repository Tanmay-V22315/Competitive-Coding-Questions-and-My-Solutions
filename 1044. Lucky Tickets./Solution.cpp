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
    
    for (int y = pow(10,x>>1)-1; y < pow(10, x); y= y+2)
    {             
        if (sumchecker(y%(int)pow(10, (x>>1)), x)==sumchecker(y - y%(int)pow(10, (x>>1)), x))
        {
            counter++;        
        }
    }
    cout <<  counter*2 << endl;
    return 0;
}
