"""
Definition ONe: 
A tree consists of a set of nodes and a set of edges that connect pairs of nodes. A tree has the following props:
	- ONe node of the tree is designated as the root node
	- Every node 'n', except the root node, is connected by an edge from exactly one other node p, where p is the 
	  parent of n
	-A unique path traverses from the root to each node
	-If each node in the tree has a maximum of two children, it is a BINARY TREE

DEF 2: A tree is either empty or consists of a root and zero or more subtrees, wach of which is also a tree. 
		The root of each subtree is connected to the root of the parent tree by an edge. 
"""

myTree = ['a', #root
	['b', #left subtree
	  ['d', [], [] ],
	  ['e', [], [] ] ], 
	['c', #right subtree
	   ['f', [], []], 
	   [] ]  
    ]

print(myTree)
print("left subtree = ", myTree[1])
print('Root = ', myTree[0])
print("Left Subtree = ", myTree[2])

#Constructs a list with a root node and two empty sublists for the children
def BinaryTree(r):
	return [r, [], []]

def insertLeft(root, ,newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [newBranch, t,[]])
	else: 
		root.insert(1, [newBranch, [], []])
	return root

def insertRight(root, newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [newBranch, [], t])
	else:
		root.insert(2, [newBranch, [], []])
	return root

#Access Functions for getting and setting the root value
def getRootVal(root):
	return root[0]

def setRootVal(root, newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

	