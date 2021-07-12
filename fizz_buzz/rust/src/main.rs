fn main() {
    let fiz1_var = 3;
    let fiz2_var = 5;
    for i in 1..100 {
        let mut somstring = String::from("");
        if i%fiz1_var == 0 {somstring.push_str("Fizz");}
        if i%fiz2_var == 0 {somstring.push_str("Buzz");}   
        if somstring==""{println!("{}", i);}
        else {println!("{}",somstring);}
    }
}

