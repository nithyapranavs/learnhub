fn main() {
    let x: i32 = 5;
    println!("{}", x);
    {
        let x = "abc";
        println!("{}", x);
    }
    let x = 'a';
    println!("{}", x);
}
