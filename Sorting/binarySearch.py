from math import floor
"""
Binary Search: 
*Assumes that the array is SORTED*

Space Complexity: O(1)
TIme Complexity:
---------------
Worst Case: O(log n)
Best Case: O(1)
Average Case: O(log n)
"""
alist = [4, 15, 23, 36, 48, 51, 62, 74, 99, 101, 234]
targNum = 15

def binarySearch(alist, numElms, targetVal):
	left = 0
	right = numElms - 1
	while left <= right:
		m = floor((left+right) / 2)
		if alist[m] < targetVal:
			left = m + 1
		elif alist[m] > targetVal:
			right = m - 1
		else: 
			return m
	return False

if(binarySearch(alist, len(alist), targNum) == False): 
	print(str(targNum) +  " was not found in the list")
else: 
	print(str(targNum) + " is in index " + str(alist.index(targNum)))


"""
DUPLICATE ELEMENTS
----------------
What if the arraylist contains duplicate elements? 
Example: [1, 2, 3, 4, 4, 5, 6, 7] and the target was 4. The regular algorithm would return the
4th element. In certain situations it may be necessary to find either the leftmost element or 
the rightmost element. 

"""

blist = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9]

# Binary Search Leftmost
def binarySearchLeftmost(alist, numElms, targetVal):
	left = 0
	right = numElms
	while left <= right:
		m = floor((left+right)/2) 
		if alist[m] < targetVal:
			left = m + 1
		else:
			right = m
	return left 

#Binary Search Rightmost
def binarySearchRightmost(alist, numElms, targetVal):
	left = 0
	right = numElms
	while left <=right:
		m = floor((left+right)/2)
		if alist[m] <= targetVal:
			left  = m + 1
		else:
			right = m
	return left - 1