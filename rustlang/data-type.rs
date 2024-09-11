use std::any::type_name;

fn type_of<T>(_: T) -> &'static str {
    type_name::<T>()
}

fn main() {
    let x: char = 'a';
    println!("x = {}", x);

    let mut tup: (i8,  char, f32) = (1, 'x', 3.2);
    tup.0 = 2;
    println!("tup {} {}",tup.0, tup.1);

    let mut arr = [1, 2, 3, 5];
    let arr2: [i32;5] = [1, 2, 3, 4, 5];

    arr[2] = 1;
    println!("arr {}", arr[2]);

    let size: isize = 5;
    println!("{}", type_of(size));
}
