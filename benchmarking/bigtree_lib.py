# https://bigtree.readthedocs.io/en/latest/

import bigtree as bt
import random

# Generate tree of abritray depth
nNodes = 1000

def generateRandomTree():
    # Initial Nodes
    btTree = bt.Node('root')
    members = [btTree]
    n = 1
    while n <= nNodes:
        id = str(random.getrandbits(100))
        payload = random.getrandbits(10)
        randomMember = random.choice(members)
        newbtNode = bt.Node(id, payload = payload, parent = randomMember)
        members.append(newbtNode)
        n = n+1
    return members, btTree

def find_node_by_name():
    members, btTree = generateRandomTree()
    for member in members:
        bt.find(btTree, lambda node: node.node_name == member.node_name)
        
def move_children():
    members, btTree = generateRandomTree()
    for i in range(30):
        randomChild = random.choice(members)
        randomNewParent = random.choice(members)
        while bt.find(randomChild, lambda node: node.name == randomNewParent.node_name) != None or randomChild.node_name == randomNewParent.node_name:
            randomChild = random.choice(members)
        randomChild.parent = randomNewParent