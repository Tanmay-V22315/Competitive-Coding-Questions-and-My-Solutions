//C++ solution, for dat speed!
#include <iostream>
#include <cmath>

using namespace std;

#define FHALF(b) (b>>1) //This is not really important and doesn't help with readability but I just wanted to get acquainted with the syntax


int sumchecker(int internum, unsigned char numberOfDigits) //This function returns the sum of digits (requires the current number and number of digits)
{
    int sum = 0;
    for (int i=0; i < numberOfDigits; i++) //This for-loop returns the sum of all the digits using modulus and divison-by-10 so that the last digit is removed
    {
        sum = sum + (internum%10); //Get the last digit and add it to sum and assign that to the sum variable
        internum = internum/10; //Get rid of the last digit since it has been dealt with
    }
    return sum;
}

//------------------------------------------------------------------------------------------------------------------------------------------------------------------//

int main()
{   
    //User Interaction
    int x;
    cout << "Number of digits: " ;
    cin >> x; //Input 

    //Initialize Counter to keep track of all satisfying values
    int counter = 0;
    int *ptr;
    ptr = &counter;


    //These numbers are re-used a lot in the for loop so there's really no point in having to calculate all of these again and again
    int Multiplier1 = pow(10,FHALF(x)); 
    int Multiplier2 = pow(10,x);


    /*This is where it all goes down
    -There is no point in checking the first few numbers (for example 0001, 00001244) and it just wastes computation time anyway so those have been completely trimmed out
    -There are as many even numbers that satisfy this as there are odd so it's just better to check for all evens and then multiply it by 2
    -TODO: There are a few numbers which are shuffled versions of an already checked number (Example: {1735:(1753,7153,7135,3571......and so on)})
     and those would need to be checked as well which wastes more time. 
    */
    for (int y = Multiplier1-1; y < Multiplier2; y= y+2) 
    {             
        if (sumchecker(y%Multiplier1, x)==sumchecker(y - y%Multiplier1, x)) //Condition checking (If true add 1 to counter)
        {
            *ptr = *ptr +1; //Adding 1 to the value stored at the memory address
        }
    }
    cout <<  *ptr*2 << endl; //Multiplying by two since we only checked for even numbers 
    return *ptr*2;
}
