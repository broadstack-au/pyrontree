# https://github.com/caesar0301/treelib/tree/master

import treelib as tl
import random

# Generate tree of abritray depth
maxRootChildren = 5
nNodes = 1000

def generateRandomTree():
    # Initial Nodes
    tlTree = tl.Tree()
    tlTree.create_node('root','root')
    members = ['root']
    n = 1
    while n <= nNodes:
        id = str(random.getrandbits(100))
        payload = random.getrandbits(10)
        randomMemberId = random.choice(members)
        tlTree.create_node(id,id,data = payload, parent = randomMemberId)
        members.append(id)
        n = n+1
    return members, tlTree

def find_nodes_by_name():
    members, tlTree = generateRandomTree()
    for member in members:
        # tlTree.filter_nodes(lambda node: node.identifier == member)
        # NOTE: The following function is a dictionary lookup.
        tlTree.get_node(member)

def move_children():
    members, tlTree = generateRandomTree()
    for i in range(30):
        randomChild = random.choice(members)
        randomNewParent = random.choice(members)
        while tlTree.is_ancestor(randomChild, randomNewParent) or randomChild == randomNewParent:
            randomChild = random.choice(members)
        tlTree.move_node(randomChild, randomNewParent)