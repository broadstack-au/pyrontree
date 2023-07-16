# Benchmarking

### Rationale

1. All Tree implementations aren't equal. 
2. It's good to have a comparison.

### Libraries (python):

1. bigtree - Version : 0.9.5
    - Repo:
        - https://github.com/kayjan/bigtree
    - Doco:
        - https://bigtree.readthedocs.io/en/latest/
    - install cmd: 
        - pip install bigtree

1. treelib - Version : 1.6.4
    - Repo: 
        - https://github.com/caesar0301/treelib/blob/master/treelib/tree.py
    - Doco: 
        - https://treelib.readthedocs.io/en/latest/
    - install cmd: 
        - pip install treelib

1. simpletree3 - Version : 1.0.10
    - Repo:
        - https://github.com/arcombe012/simpletree3
    - Doco:
        - https://pypi.org/project/simpletree3/
    - install cmd: 
        - pip install simpletree3

### BenchMark Fucntions:

Are fairly scrappy.
Only track time, not memory.

1. Generate a tree with ~ 1000 Nodes, by randomly selecting existing nodes and adding a child to them.
2. Find all nodes in the tree once (of a tree generated by 1.).
3. Move 30 randomly selected Nodes around in the tree (to random locations in a tree generated by 1.).

### Results:

1. Generate - 100 BenchMark Function Calls (each call generates a random tree with 1000 nodes)
    - bigtree_lib    took 0.3980016670 seconds, on average each run took 0.0039800167 seconds
    - tree_lib       took 0.1970255000 seconds, on average each run took 0.0019702550 seconds
    - simpletree_lib took 0.0972802080 seconds, on average each run took 0.0009728021 seconds

2. Find - 100 BenchMark Function Calls (each call finds EVERY node in the tree, once)
    - bigtree_lib    took 16.9774277500 seconds, on average each run took 0.1697742775 seconds
    - tree_lib       took 0.2062751250 seconds, on average each run took 0.0020627512 seconds
    - simpletree_lib took 16.6338677080 seconds, on average each run took 0.1663386771 seconds

3. Move - 33 BenchMark Function Calls (each call moves 30 nodes to random locations)
    - bigtree_lib    took 0.1349361250 seconds, on average each run took 0.0040889735 seconds
    - tree_lib       took 0.0707031660 seconds, on average each run took 0.0021425202 seconds
    - simpletree_lib took 0.0341277500 seconds, on average each run took 0.0010341742 seconds

### Notes:

1. Tree_lib implements a dictionary lookup for retrieving the nodes by ID, all other libraries are doing a tree traversal. (I'm pretty sure I haven't buggered up the benchmark function).

From: https://github.com/caesar0301/treelib/blob/master/treelib/tree.py 
`
    line 507:
    def get_node(self, nid):
        """
        Get the object of the node with ID of ``nid``.

        An alternative way is using '[]' operation on the tree. But small difference exists between them:
        ``get_node()`` will return None if ``nid`` is absent, whereas '[]' will raise ``KeyError``.
        """
        if nid is None or not self.contains(nid):
            return None
        return self._nodes[nid]
    
    line 83: 
    #: dictionary, identifier: Node object
        self._nodes = {}
`