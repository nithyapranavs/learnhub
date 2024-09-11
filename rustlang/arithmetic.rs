use std::io;

//use std::any::type_name;
//fn type_of<T>(_: T) -> &'static str {
//    type_name::<T>()
//}

fn main() {
    let x: u8 = 205;  // 0 - 255
    let y: i8 = 10; // -128 - -127

    let z = x / y as u8;
    println!("z = {}", z);

    // convert input string to int 
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("failed to read line");

    let int_input: i64 = input.trim().parse().unwrap(); // trim removes \n ig

    println!("input = {}", int_input + 2);

}
