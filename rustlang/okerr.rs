// Function to divide two numbers
fn divide(x: f64, y: f64) -> Result<f64, &'static str> {
    if y == 0.0 {
        Err("Division by zero")
    } else {
        Ok(x / y)
    }
}

fn main() {
    // Example of using Result to handle division by zero error
    match divide(10.0, 2.0) {
        Ok(result) => println!("Result of division: {}", result),
        Err(err) => println!("Error: {}", err),
    }
	
	match divide(10.0, 0.0) {
        Ok(result) => println!("Result of division: {}", result),
        Err(err) => println!("Error: {}", err),
    }
}

