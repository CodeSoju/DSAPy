"""
6.5 Nodes and References
Define a class that has attributes for the root value, as well as the left and right subtrees. SInce this 
representation....

"""

class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	#To add a left child to the tree, we will create a new binary tree object and set the 'left' attribute
	# of the root to refer to this new object
	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

#Accessor Functions
	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self, obj):
		self.key = obj 

	def getRootVal(self):
		return self.key

#Creating a tree and adding node to it
"""
myTree = BinaryTree('a')
print("Tree Root Value: ", myTree.getRootVal())
print("Current left child: ", myTree.getLeftChild())
myTree.insertLeft('b')
print("After Insertion LeftChild is: ", myTree.getLeftChild())
print("Current right child: ", myTree.getRightChild())
myTree.insertRight('c')
print("After Insertion of rightChild: ", myTree.getRightChild().getRootVal())
"""

#preOrder for a BinaryTree
def preorder(self):
	print(self.key)
	if self.leftChild:
		self.leftChild.preorder()
	if self.rightChild:
		self.rightChild.preorder()

