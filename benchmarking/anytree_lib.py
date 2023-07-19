# https://bigtree.readthedocs.io/en/latest/

import anytree as at
import random

# Generate tree of abritray depth
nNodes = 1000

def generateRandomTree():
    # Initial Nodes
    atTree = at.Node('root')
    members = [atTree]
    n = 1
    while n <= nNodes:
        id = str(random.getrandbits(100))
        payload = random.getrandbits(10)
        randomMember = random.choice(members)
        newAtNode = at.Node(id, payload = payload, parent = randomMember)
        members.append(newAtNode)
        n = n+1
    return members, atTree

def find_node_by_name():
    members, atTree = generateRandomTree()
    for member in members:
        # Seems to be an oddity with anytree.find() where it returns all the chilren associated with a node, not just the single node
        r = at.findall(atTree, lambda node: node.name == member.name)
        
def move_children():
    members, atTree = generateRandomTree()
    for i in range(30):
        randomChild = random.choice(members)
        randomNewParent = random.choice(members)
        while ((randomChild in randomNewParent.ancestors) == True) or randomChild.name == randomNewParent.name:
            randomChild = random.choice(members)
            randomNewParent = random.choice(members)
        randomChild.parent = randomNewParent