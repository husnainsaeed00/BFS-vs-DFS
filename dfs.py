# First Method::Recursive
#we are using the built it call stack for ruccursion wchich is very slow

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right
    def __str__(self):
        return "Node(" + str(self.value) + ")"
    

def walk(tree):
    if tree is None:
        return
    
    print(tree)
    walk(tree.left)
    walk(tree.right)

    
#Second mehtod::Iterative
# We are usinng our own built in Stack wchich is using explicit stack // python provides the limit of 1000 memory units.
def walk2(tree, stack):
    stack.append(tree)
    while len(stack)>0:
        node=stack.pop()
        if node is not None:
            print(node)
            stack.append(node.right)
            stack.append(node.left)

mytree = Node('A', Node('B', Node('C',Node('D'),Node('E')),Node('C', Node('F'),Node('G'))))
stack = []
walk2(mytree, stack)
