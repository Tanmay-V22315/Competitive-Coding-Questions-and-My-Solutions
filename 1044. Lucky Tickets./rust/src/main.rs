fn main() {
    let mut counter = 0; //Counting 
    let number_of_digits = 8; //Number of digits, this is supposed to be the user input
    let w = i32::pow(10,number_of_digits>>1); 
    let upnum = i32::pow(10,number_of_digits);
    let begnum = i32::pow(10,number_of_digits>>1)-1;
    let stepnum = 2;


    for i in (begnum..upnum).step_by(stepnum) {
        if summer(i%w)==summer(i/w){counter += 1}
    }
    println!("Final Counter = {}", counter*stepnum);
} 


//Function that returns the sum of the digits of the input number
fn summer(mut x : i32) -> i32 {
    let mut sum = 0;
    while x>=1 {
        sum = sum + x%10;
        x = x/10;
    }
    return sum;
}
