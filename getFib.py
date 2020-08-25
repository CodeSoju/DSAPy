#Iterative Solution
def getFib(position):
	if position == 0:  
		return 0
	if position == 1:  
		return 1

	first = 0 
	second = 1 
	nxt = first + second
# for(int k = 1; k <= c; k++)  ---- C/C++
# for k in 
#
	for i in range(2, position):
		first = second
		second = nxt 
		nxt = first + second
	
	return nxt

#Recursive Solution
def getFibRecursive(position):
	if position == 0 or position == 1:
		return position
	return getFibRecursive(position - 1) + getFibRecursive(position - 2)

print("Iterative Solution: " + str(getFib(6)))
print("Recursive Solution: " + str(getFibRecursive(6)))

#If you want to cast from int to string ---> str(number)

#As we learned, recursion has its drawbacks, the number of recursive calls grows exponentially 
# according to n 