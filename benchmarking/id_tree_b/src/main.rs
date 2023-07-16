#![feature(test)]
extern crate test;
use id_tree::*;
use rand::seq::SliceRandom;
use rand::Rng;
// use bencher::Bencher;

pub fn add1(n: i32) -> i32 {
    n + 1
}

pub fn main() {
    use id_tree::InsertBehavior::*;

    //      0
    //     / \
    //    1   2
    //   / \
    //  3   4
    let mut tree: Tree<i32> = TreeBuilder::new()
        .with_node_capacity(5)
        .build();

    let root_id: NodeId = tree.insert(Node::new(0), AsRoot).unwrap();
    let child_id: NodeId = tree.insert(Node::new(1), UnderNode(&root_id)).unwrap();
    tree.insert(Node::new(2), UnderNode(&root_id)).unwrap();
    tree.insert(Node::new(3), UnderNode(&child_id)).unwrap();
    tree.insert(Node::new(4), UnderNode(&child_id)).unwrap();
}

pub fn generate_random_tree() -> (Vec<NodeId>, Tree<i32>) {
    use id_tree::InsertBehavior::*;

    const NNODES: usize = 1000;
    // nNodes = 1000
    
    let mut tree: Tree<i32> = TreeBuilder::new()
        .with_node_capacity(NNODES)
        .build();

    let mut node_id_store: Vec<NodeId> = Vec::new();
    let root_id: NodeId = tree.insert(Node::new(0), AsRoot).unwrap();
    node_id_store.push(root_id);
    for _i in 1..NNODES {
        let id: i32 = rand::thread_rng().gen_range(0..2147483647);
        let a_node_id = node_id_store.choose(&mut rand::thread_rng()).unwrap();
        let child_id: NodeId = tree.insert(Node::new(id), UnderNode(a_node_id)).unwrap();
        node_id_store.push(child_id);
    }
    
    return (node_id_store, tree);
}

pub fn find_nodes_by_name() {

    let (node_id_store, tree) = generate_random_tree();
    println!("{}", node_id_store.len());
    for node_id in &node_id_store {
        let _node_ref_result: Result<&Node<i32>, NodeIdError> = tree.get(node_id);
    }
}

//  Reference for #[Bench]
// https://doc.rust-lang.org/nightly/unstable-book/library-features/test.html


#[cfg(test)]
mod tests {
    use super::*;
    use test::Bencher;
 
    #[test]
    fn it_works() {
        assert_eq!(1, add1(0));
    }

    #[test]
    fn tree_works() {
        let (node_id_store, tree) = generate_random_tree();
        assert_eq!(node_id_store.len(), 1000);
    }

    #[bench]
    fn bench_add1(b: &mut Bencher) {
        b.iter(|| add1(0));
    }

    #[bench]
    fn bench_generate_random_tree(b: &mut Bencher) {
        b.iter(|| generate_random_tree());
    }

    #[bench]
    fn bench_find_nodes_by_name(b: &mut Bencher) {
        b.iter(|| find_nodes_by_name());
    }
   
}


