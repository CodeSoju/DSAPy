"""
INSERTION SORT:
T.C.:
Worst Case: O(n^2) comparisons and swaps
Best-Case: O(n) comparisons, O(1) swaps
Averge-case: O(n^2) comparisons and swaps

Always maintains a sorted sublist in the lower positions of the list. Each new item is then "inserted" back into 
the previous sublist such that the sorted sublist is one item larger. 

THe maximum number of comparisons for an insertion sort is the sum of the first n-1 integers. 
THis is O(n^2). HOwever the best case, only one comparison needs to be done on each pass. THis 
would be the case for an already sorted list. 
"""
import time 



fileName = 'nums.txt'

def insertionSort(alist):
	for index in range(1, len(alist)):

		currentValue = alist[index]
		position = index

		while position > 0 and alist[position - 1] > currentValue:
			alist[position] = alist[position -1]
			position = position - 1

		alist[position] = currentValue

alist = []
insertionSort(alist)
print(alist)

def createListFromTextOfNums(fileName):
	theFile = open(fileName, "r")
	alist =[]

	for val in theFile.read().split():
		alist.append(int(val))
	theFile.close()

	return alist

alist= createListFromTextOfNums(fileName)
#print(type(alist[2]))

start = time.time()
insertionSort(alist)
end = time.time()

print("It took: " + str(end-start) + "seconds")
#print(alist)