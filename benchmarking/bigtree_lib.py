# https://bigtree.readthedocs.io/en/latest/

import bigtree as bt
import random

# Generate tree of abritray depth
maxRootChildren = 5
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

# def generateRandomTree():
#     # Initial Nodes
#     btTree = bt.Node('root')
#     members = []
#     # Generate a random number children at the root
#     nNodes = random.randint(1,maxRootChildren)
#     for i in range(nNodes):
#         id = str(random.getrandbits(100))
#         payload = random.getrandbits(10)
#         newbtNode = bt.Node(id, payload = payload, parent = btTree)
#         members.append(newbtNode)
#     stages = [3,6,12,24,48,96,192,384]
#     # at each stage create a set number of children on random nodes
#     for i in range(len(stages)):
#         n = stages[i]
#         newMembers = []
#         for nNew in range(n):
#             id = str(random.getrandbits(100))
#             payload = random.getrandbits(10)
#             randomMember = random.choice(members)
#             newbtNode = bt.Node(id, payload = payload, parent = randomMember)
#             newMembers.append(newbtNode)
#         members.extend(newMembers)
#     return members, btTree

def find_node_by_name():
    members, btTree = generateRandomTree()
    for member in members:
        bt.find(btTree, lambda node: node.name == member.node_name)
        
def move_children():
    members, btTree = generateRandomTree()
    for i in range(30):
        randomChild = random.choice(members)
        randomNewParent = random.choice(members)
        while bt.find(randomChild, lambda node: node.name == randomNewParent.node_name) != None or randomChild.node_name == randomNewParent.node_name:
            randomChild = random.choice(members)
        randomChild.parent = randomNewParent