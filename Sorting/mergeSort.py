"""
Merge Sort : an good example of a Divide and Conquer approach to an algorthim

O((# comparisons per step) (# of steps))
O(n log (n))

Auzilary Space -> O(n)
"""

def mergeSort(alist):
	print("Splitting", alist)
	if len(alist) > 1:
		mid = len(alist)//2
		leftHalf = alist[:mid]
		rightHalf = alist[mid:]

		mergeSort(leftHalf)
		mergeSort(rightHalf)

		i = 0
		j = 0
		k = 0

		while i < len(leftHalf) and j < len(rightHalf):
			if leftHalf[i] < rightHalf[j]:
				alist[k] = leftHalf[i]
				i += 1
			else: 
				alist[k] = rightHalf[j]
