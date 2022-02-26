
fn main() {
    // normal comment

    /*
    multiline
    comment
    */

    printing_basics();
    printing_structs();

    primitives();
}

fn printing_basics() {
    // basic formatting
    print!("Hello, world!\n");
    println!("{}", "Hello, world!");
    println!("{1}, {0}", "world!", "Hello");
    println!("{greeting}, {subject}", greeting="Hello", subject="world!");

    // special formatting
    println!("Binary: {:b} Hex: {:x} Octal: {:o}", 10, 10, 10);

    // padding
    println!("{:4}", 1);
    println!("{:<4}", 1);
    println!("{:>4}", 1);
    println!("{:^4}", 1);
    println!("{:^4}", "foo");

    // precision
    println!("{:.4}", 1.23456);

    // alignment
    println!("{:<1$}", "foo", 4);
    println!("{:>1$}", "foo", 4);
    println!("{:^1$}", "foo", 4);
    println!("{:^1$}", "foo", 4);
}

use std::fmt;

fn printing_structs() {
    // Structs are different! You have to define a fmt::Debug implementation for it to be printable
    // In a pinch, you can use the #[derive(Debug)] attribute:
    #[derive(Debug)]
    struct Structure(i32);

    println!("This struct `{:?}` can now be printed!", Structure(3));
    println!("This struct `{:#?}` can also be pretty printed!", Structure(3));

    // You can also define your own custom formatting for your structs
    // This is useful for printing structs that have a lot of fields
    // or if you want to print them in a particular order

    struct Structure2 {
        first: i32,
        second: i32,
        third: i32,
    }

    impl fmt::Display for Structure2 {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            write!(f, "({}, {}, {})", self.first, self.second, self.third)
        }
    }

    println!("This struct `{}` can now be printed!", Structure2 { first: 1, second: 2, third: 3 });

    // There are more complicated formatting options for structs, but we'll get to those later (maybe lol)
}

fn primitives() {
    // Scalar types
    println!("Signed integers:        {} {} {} {} {} {}", 1i8, 1i16, 1i32, 1i64, 1i128, 1isize); // default integer size is 32-bit
    println!("Unsigned integers:      {} {} {} {} {} {}", 1u8, 1u16, 1u32, 1u64, 1u128, 1usize); // default integer size is 32-bit
    println!("Floating point numbers: {} {}", 1f32, 1f64);                                       // default floating point size is 64-bit
    println!("Bools:                  {} {}", true, false);
    println!("Chars:                  {}", 'a');
    println!("Strings:                {}", "a");
    println!("Byte arrays:            {:?}", b"a");
    println!("Raw strings:            {}", r"a");

    // this is a special type, which can only have the value `()` (empty tuple)
    println!("Unit type:              {}", ());

    // Compound types
    println!("Tuples:                 {:?}", (1u8, 2u16, 3u32, 4u64, 5u128, 6usize));
    println!("Arrays:                 {:?}", [1u8; 5]);
    println!("Vectors:                {:?}", vec![1u8; 5]);
}
