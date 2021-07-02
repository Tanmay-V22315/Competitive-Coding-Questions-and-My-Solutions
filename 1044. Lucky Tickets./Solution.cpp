//C++ solution, for dat speed!
// Can still use some optimization but this is just for learning the language.
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
    for (int y = 0; y < pow(10, x); y++)
    {
    
        
        if (sumchecker(y%(int)pow(10, (x>>1)), x)==sumchecker(y - y%(int)pow(10, (x>>1)), x))
        {
            counter++;
        }
    }
    cout <<  counter << endl;
    return 0;
}
