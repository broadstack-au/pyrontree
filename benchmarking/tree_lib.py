# https://github.com/caesar0301/treelib/tree/master

import treelib as tl
import random

# Generate tree of abritray depth
maxNodeSize = 5
maxDepth = 10

def generateRandomTree():
    # Initial Nodes
    tlTree = tl.Tree()
    tlTree.create_node('root','root')
    members = []
    # Generate a random number children at the root
    nNodes = random.randint(1,maxNodeSize)
    for i in range(nNodes):
        id = str(random.getrandbits(100))
        members.append(id)
        payload = random.getrandbits(10)
        tlTree.create_node(id,id, data = payload, parent = 'root')
    stages = [3,6,12,24,48]
    # stages = [3,3,3]
    for i in range(len(stages)):
        n = stages[i]
        newMembers = []
        for nNew in range(n):
            id = str(random.getrandbits(100))
            newMembers.append(id)
            payload = random.getrandbits(10)
            randomMemberId = random.choice(members)
            tlTree.create_node(id,id,data = payload, parent = randomMemberId)
        members.extend(newMembers)
    return members, tlTree

def find_nodes_by_name():
    members, tlTree = generateRandomTree()
    for member in members:
        tlTree.filter_nodes(lambda node: node.identifier == member.identifier)
        # NOTE: This following function is about the same speed as the above, however the other functions don't seem to have it
        # tlTree.get_node(member)

def move_children():
    members, tlTree = generateRandomTree()
    for i in range(30):
        randomChild = random.choice(members)
        randomNewParent = random.choice(members)
        while tlTree.is_ancestor(randomChild, randomNewParent) or randomChild == randomNewParent:
            randomChild = random.choice(members)
        tlTree.move_node(randomChild, randomNewParent)