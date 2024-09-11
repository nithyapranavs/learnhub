fn add_num(x: i32, y: i32) -> i32 {
    x + y
    // or return x + y, if return is there ';' can be added
}

fn main() {
    let number = {
        let x = 3;
        x + 2 // its now expression, adding ; becomes statement
    };

    println!("number = {}", number);
    
    println!("number = {}", add_num(4,5));

}
