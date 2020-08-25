"""
Quick Sort uses divide and conquer to gain the same advantages as the merge sort, while not 
using additional storage.
The trade-off: it is possible that the list may not be divided in half. This diminish the 
performance. 

QS chooses a value, usually called the PIVOT VALUE. The role of the pivot value is to assist
w/ splitting the list. Resulting in the final position of the pivot value, called 
the split point ,this will be used to divide the list for subsequent calls to the QS. 

Time Complexity:
Best Case: O(n logn)
Worst Casr O(n^2)
"""
import random

alist = []
	# Produces Random Numbers 
for x in range(10):
	x = random.randint(1, 1001)
	alist.insert(0, x)

clist = [2, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 0, 0, 1, 1,  2, 2, 2, 1, 1, 0, 0, 1, 2, 1, 2, 1,1, 1, 0, 0, 2, 2, 2, 1, 2, 1, 2,1, 2]

print("Original List: " + str(alist))

def quickSort(alist):
	quickSortHelper(alist, 0, len(alist)- 1)

def quickSortHelper(alist, first, last):
	if first < last: 
		splitPoint = partition(alist, first, last)

		quickSortHelper(alist, first, splitPoint - 1)
		quickSortHelper(alist, splitPoint + 1, last)

def partition(alist, first, last):
	pivotValue = alist[first]

	leftMark = first + 1
	rightMark = last

	done = False
	while not done: 
		while leftMark <= rightMark and alist[leftMark] <= pivotValue:
			leftMark = leftMark + 1

		while alist[rightMark] >= pivotValue and rightMark >= leftMark:
			rightMark = rightMark - 1

		if rightMark < leftMark:
			done = True
		#Swap
		else:
			temp = alist[leftMark]
			alist[leftMark] = alist[rightMark]
			alist[rightMark] = temp
	#END MAIN WHILE
	temp = alist[first]
	alist[first] = alist[rightMark]
	alist[rightMark] = temp

	return rightMark 

"""
quickSort(alist)
print("\nAfter QuickSort: " + str(alist))


print("\nBefore QuickSort: " + str(clist))
quickSort(clist)
print("\nAfter QuickSort: " + str(clist))
"""
"""
3 Way Quick Sort (Dutch National Flag)

"""
blist = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4]
print("Original list: " + str(clist))

def threeWaySort(alist):
	lo = 0
	hi = len(alist) - 1
	mid = 0

	while  mid <= hi:
		if alist[mid] == 0:
			alist[lo], alist[mid] = alist[mid], alist[lo]
			lo = lo + 1
			mid = mid + 1
		elif alist[mid] == 1:
			mid = mid + 1
		else:
			alist[mid], alist[hi] = alist[hi], alist[mid]
			hi = hi - 1
	return alist

threeWaySort(clist)
print("After 3-Way QS:" + str(clist))