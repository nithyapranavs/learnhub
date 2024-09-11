pub struct LinkedList<T> {
    pub val: Option<T>;
    pub next: Option<box<LinkedList<T>>>;
}

impl LinkedList<u32> {
    pub fn new() -> LinkedList<u32>{
        LinkedList {
            val: None,
            next: None,
        }
    }
}
