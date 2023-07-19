import bigtree_lib
import tree_lib
import simpletree_lib
import anytree_lib
import timeit

nTests = 1

print("Testing generateRandomTree {} times".format(nTests))

t1 = timeit.Timer(bigtree_lib.generateRandomTree).timeit(number = nTests)
t2 = timeit.Timer(tree_lib.generateRandomTree).timeit(number = nTests)
t3 = timeit.Timer(simpletree_lib.generateRandomTree).timeit(number = nTests)
t4 = timeit.Timer(anytree_lib.generateRandomTree).timeit(number = nTests)
t1avg = t1/nTests
t2avg = t2/nTests
t3avg = t3/nTests
t4avg = t4/nTests

print("\nbigtree_lib    took {:.10f} seconds, on average each run took {:.10f} seconds".format(t1, t1avg))
print("tree_lib       took {:.10f} seconds, on average each run took {:.10f} seconds".format(t2, t2avg))
print("simpletree_lib took {:.10f} seconds, on average each run took {:.10f} seconds".format(t3, t3avg))
print("anytree_lib    took {:.10f} seconds, on average each run took {:.10f} seconds".format(t4, t4avg))

nTests = 1

print("\nTesting Find_Every_Node_By_Name {} times".format(nTests))

t1 = timeit.Timer(bigtree_lib.find_node_by_name).timeit(number = nTests)
t2 = timeit.Timer(tree_lib.find_nodes_by_name).timeit(number = nTests)
t3 = timeit.Timer(simpletree_lib.find_node_by_name).timeit(number = nTests)
t4 = timeit.Timer(anytree_lib.find_node_by_name).timeit(number = nTests)
t1avg = t1/nTests
t2avg = t2/nTests
t3avg = t3/nTests
t4avg = t4/nTests

print("\nbigtree_lib    took {:.10f} seconds, on average each run took {:.10f} seconds".format(t1, t1avg))
print("tree_lib       took {:.10f} seconds, on average each run took {:.10f} seconds".format(t2, t2avg))
print("simpletree_lib took {:.10f} seconds, on average each run took {:.10f} seconds".format(t3, t3avg))
print("anytree_lib    took {:.10f} seconds, on average each run took {:.10f} seconds".format(t4, t4avg))

nTests = 33

print("\nTesting move_children {} times, each run moves 30 children".format(nTests))

t1 = timeit.Timer(bigtree_lib.move_children).timeit(number = nTests)
t2 = timeit.Timer(tree_lib.move_children).timeit(number = nTests)
t3 = timeit.Timer(simpletree_lib.move_children).timeit(number = nTests)
t4 = timeit.Timer(anytree_lib.move_children).timeit(number = nTests)

t1avg = t1/nTests
t2avg = t2/nTests
t3avg = t3/nTests
t4avg = t4/nTests

print("\nbigtree_lib    took {:.10f} seconds, on average each run took {:.10f} seconds".format(t1, t1avg))
print("tree_lib       took {:.10f} seconds, on average each run took {:.10f} seconds".format(t2, t2avg))
print("simpletree_lib took {:.10f} seconds, on average each run took {:.10f} seconds".format(t3, t3avg))
print("anytree_lib    took {:.10f} seconds, on average each run took {:.10f} seconds".format(t4, t4avg))
