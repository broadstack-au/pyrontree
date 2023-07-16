# https://github.com/arcombe012/simpletree3

import simpletree3 as si
import random

# Generate tree of abritray depth
maxRootChildren = 5
nNodes = 1000

def generateRandomTree():
    # Initial Nodes
    siTree = si.SimpleNode('root')
    members = [siTree]
    n = 1
    while n <= nNodes:
        id = random.getrandbits(100)
        payload = random.getrandbits(10)
        randomMember = random.choice(members)
        newNode = si.SimpleNode(key = id, parent = randomMember, data = payload)
        members.append(newNode)
        n = n+1
    return members, siTree

def find_node_by_name():
    members, siTree = generateRandomTree()
    for member in members:
        si.find_first_node(siTree, member.key)

def move_children():
    members, siTree = generateRandomTree()
    for i in range(30):
        randomChild = random.choice(members)
        randomNewParent = random.choice(members)
        while (randomChild in randomNewParent.ancestors) or (randomChild.key == randomNewParent.key) or randomChild.is_root:
            randomChild = random.choice(members)
        randomChild.parent = randomNewParent

    randomChild = random.choice(members)
    randomNewParent = random.choice(members)
    randomChild in randomNewParent.ancestors
