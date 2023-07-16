# https://github.com/arcombe012/simpletree3

import simpletree3 as si
import random

# Generate tree of abritray depth
maxRootChildren = 5

def generateRandomTree():
    # Initial Nodes
    siTree = si.SimpleNode('root')
    members = []
    # Generate a random number children at the root
    nNodes = random.randint(1,maxRootChildren)
    for i in range(nNodes):
        id = random.getrandbits(100)
        payload = random.getrandbits(10)
        newNode = si.SimpleNode(key = id, parent = siTree, data = payload)
        members.append(newNode)
    stages = [3,6,12,24,48,96,192,384]
    # stages = [3,3,3]
    for i in range(len(stages)):
        n = stages[i]
        newMembers = []
        for nNew in range(n):
            id = random.getrandbits(100)
            payload = random.getrandbits(10)
            randomMember = random.choice(members)
            newNode = si.SimpleNode(key = id, parent = randomMember, data = payload)
            newMembers.append(newNode)
        members.extend(newMembers)
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
