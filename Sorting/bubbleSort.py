"""
Bubble Sort: An example of an inplace sorting algo. 
Space Complexity: O(1)
Time Cimplexity:
-------------------
Worst Case -> O(n^2)
Average Case -> O(n^2)

Best Case -> O(n)
"""

"""
THe exchange op, AKA swap, is the swapping of two elements in a list requiring
a temporary storage location  (an additional memory location):

temp = alist[i]
alist[i] = alist[j]
alist[j] = temp
"""
alist = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

def bubbleSort(alist):
	iterats = 0
	for passnum in range(len(alist)-1, 0, -1):
		for i in range(passnum) :
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp 
				#print("Iterate " + str(iterats) + ": " + str(alist))
		iterats+= 1
		print("Iterate " + str(iterats) + ": " + str(alist))

bubbleSort(alist)
print(alist)	


"""
A bubble sort is considered the most inefficient sorting method since it must exchange items
before the final location is known . Resulting in waster ops which are very costly. 
Bubble sort can be modified to stop early if it finds that the list has become sorted. 

Short Bubble -> Recognizes the sorted list and stops
"""
blist = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
pint("\n")

def shortBubbleSort(alist):
	iterats = 1
	exchanges = True
	passnum = len(alist) - 1
	while passnum > 0 and exchanges:
		exchanges = False
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				exchanges = True
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp 
				#print("\nIteration " + str(iterats) + ": " + str(alist))
				#iterats += 1
		passnum = passnum - 1
		print("Iteration " + str(iterats) + ": " + str(alist))
		iterats += 1


shortBubbleSort(blist)
print("After Short Bubble Sort: "+ str(blist))

