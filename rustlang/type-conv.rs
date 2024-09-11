fn main() {
    // Attempt to assign a floating-point value to an integer variable without explicit conversion
    //let x: i32 = 5.9; // This will result in a compilation error

    // Fix: Use explicit type conversion to assign the floating-point value to the integer variable
    let y: i32 = 5.9 as i32;

    println!("Value of y: {}", y);
	
	let z: i32 = 5.9_f32.round() as i32;

    println!("Value of z: {}", z);

    for i in 0..10 {
        println!("{}", i);
    }
}
