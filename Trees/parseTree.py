"""
First step in building a parse tree is to break up the expression string into a list of tokens. 
THere are 4 tokens: left parentheses, right parentheses, opertors, and operands

Define 4 rules:
	1. If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.
	2. If the current token is in the list ['+', '-', '/','*'], set the root value of the current node to the operator
		represented by the current token. Add a new node as the right child of the current node and descenc to the right 
		child
	3. If the current token os a number, set the root value of the current node to the number and return to the
		parent
	4. If the current token is a ')', go to the parent of the current node

We will need to keep track of the parents, one solution is to use a stack. Whenever we want to descend to a child
of the current node, we first push the current node on the stack. When we want to return to the parent of the current node, 
we pop the parent off the stack
 """
from stack import Stack 
from binaryTree import BinaryTree


def buildParseTree(fpexp):
 	fplist = fpexp.split()
 	pStack = Stack()
 	eTree = BinaryTree('')
 	pStack.push(eTree)
 	currentTree = eTree

 	for i in fplist:
 		if i == '(':
 			currentTree.insertLeft('')
 			pStack.push(currentTree)
 			currentTree = currentTree.getLeftChild()
 		elif i not in ['+', '-', '*', '/', ')']:
 			currentTree.setRootVal(int(i))
 			parent = pStack.pop()
 			currentTree = parent
 		elif i in ['+', '-', '*', '/']:
 			currentTree.setRootVal(i)
 			currentTree.insertRight('')
 			pStack.push(currentTree)
 			currentTree = currentTree.getRightChild()
 		elif i == ')':
 			currentTree = pStack.pop()
 		else:
 			raise ValueError
 	return eTree

def evaluate(parseTree):
	opers = {'+': operator.add, '-':operator.sub, '*': operator.mul, '/':operator.truediv}

	leftC = parseTree.getLeftChild()
	rightC = parseTree.getRightChild()

	if leftC and rightC:
		fn = opers[parseTree.getRootVal()]
		return fn(evaluate(leftC), evaluate(rightC))
	else:
		return parseTree.getRootVal()

def postOrderEvaluate(parseTree):
	opers = {'+': operator.add, '-':operator.sub, '*': operator.mul, '/':operator.truediv}

	res1 = None
	res2 = None

	if parseTree:
		

pt = buildParseTree("( ( 10 + 5) * 3 )")

"""
TREE TRAVERSALS:
preorder: visit the root node first, then recursively so a preorder traversal of the left subtree, followed
			by a recusive preorder traversal of the right subtree

inorder: recursively do an inorder traversal on the left subtree, visit the root node, 
		and finally do a recursive inorder traversal of the right subtree

postorder: recusively do a postorder traversal on the left subtree and right subtree followd
			by a visit to the root node. 


"""

def preorder(tree):
	if tree:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preOrder(tree.getRightChild())

def inorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		print(tree.getRootVal())
		inorder(tree.getRightChild())

def postorder(tree):
	if tree:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print(tree.getRootVal())