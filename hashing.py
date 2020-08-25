"""
KNowing that a list is ordered, we could search in logarithmic time using a binary search. 
But there is a data structure that can allow us to search in constant time (O(1)). Hashing....

a hash table is a collection of items which are not stored in such a way as to make it easy to find 
them later. Each position of the hash table, often called a lsot, can hold an item and is named 
by an integer value staring at 0. 
Initially, the hash table contains no items so every slot is empty. We can implement a hash table 
by using a list with each element initialized to the special Python value 'None'. 

THe mapping between an item and the slot where that item belongs in the hash table is called the
hash function.  THe hash function will take any item in the collection and return an integer in the 
range of slot names. between 0 and m-1.

Once the hash values has been computeed, we can insert each item into the hash table at the
designated position. This is referred to as the 'load factor'. 
	Lambda = # of items/table size.

	Now when we want to search for an item , we simply use the hash function to compute the slot name
	for the item and then check the hash table to see if it is present. This searching operation is O(1), 
	since a contant amount of time is required to compute the hash value and then index the hash table at 
	that location. 
	According to he hash function, two or more items would need to be in the same slot. This is reffered
	to as a collision)(or a clash). Clearly, collisions create a problem for the hashing technique. 

	Given a collection of items, a hash functions that maps each item into a unique slot is referred to 
	as a 'perfect hash function'. If we know the items and the collection will never change, then it is 
	possible to construct a perfect hash function. 

	One way to always have a perfect hash function is to increase the size of the hash table so that 
	each posiible value in the item range can be accommodated. This guarantess that each item 
	will have a unique slot. Although this is practical for small numbers of items, it is not feasible
	when the number of possible items is large. 

	The folsing method for constructing hash functions begins by dividing the item into equal-size pieces 
	These pieces are then added together to give the resulting hash value. 
	For example, if our tiems was a phone number 436-555-4601, we would take the digits and divide them into 
	groups of 2 (43, 65, 55, 46, 01). After the addition, 43+65+55+46+01, we get 210. If we assume out hash
	table has 11 slots, then we need to perform the extra step of dividing by 11 and keeping the remainder. 
	IN this case 210%11 = 1, so the phone number hashes to slot 1. 

	Another numerical technique for constructing a hash function is called a 'mid-square method'. We first 
	square the item, and then extractf some portion of the resulting digits. For example, if the item 
	were 44, we would first compute 44^2 = 1936. BY extracting the middle two digits, 93 and performing the 
	remainder step, we get 93%11 = 5.

	One can also create hash function for character-based items such as strings. 
"""
#print(ord('c'))  #prints 99

"""
We can take these 3 ordinal values, add them up and use the remainder method to get a hash value

"""

"""
n1 = [0 for i in range(15)]
n2 = [0] * 15

Both initalize a list with 15 zeroes
"""
words = ['Joseph', 'go', 'home']
hashtable = [0] * 10
hashT_size = len(hashtable)

def hashListWords(aList, tablesize, hashtable):
	for x in range(len(aList)):
		sum = 0
		for pos in aList[x]:
			sum = sum + ord(pos)
		hashtable[sum%tablesize] = aList[x]

hashListWords(words, hashT_size, hashtable)
print(hashtable)

def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum%tablesize

"""
INterestingly enough, anagrams will always be given the same hash value. To remedy this, we could use the position of the character
as a weight. 
"""
# use the position of the character, in order to bypass anagrams having same hashvalues
def hashMod(astring, tablesize):
	sum = 0
	position = 1
	for pos in range(len(astring)):
		sum = sum + (ord(astring[pos])*position)
		position += 1
	return sum%tablesize

print('Using Hash:\n')
print("cat: "+ str(hash('cat', 11)))
print("act: "+str(hash('act', 11)))
print("tac: "+str(hash('tac', 11)))

print("Using HashMod: \n")
print("cat: "+ str(hashMod('cat', 11)))
print("act: "+ str(hashMod('act', 11)))
print("tac: " + str(hashMod('tac', 11)))

"""
One method of resolving collisions looks into the hash table and tries to find another 
open slot to hold the item that caused the collision. A simple way to do this is start at 
the original hash value position and then move in a sequential manner throught the slots until we 
encounter 

Open Addressing: a collision resolution process where it tries to find the next open slot 
or address in the hash table. 

Linear Probing: systematically visiting each slot one at a time. 

Tthe disadvantage of linear probing is the tendency for clustering; items become clustered
in the table. Meaning that if many collisions occur at the same hash value, a number of surrounding 
slots will be filled ny the linear probing resolution. 

One solution for linear probing is to extend the LP technique so that instead of looking sequentially
for the next open slot, we skip slots, thereby more evenly distributing the items that have caused 
collisions. THie will potentially reduce the clustering that occurs.

AKA Rehashing; the general process of looking for another slot after a collision
newHashValue = rehash(oldHashValue) where
rehash(pos) = (pos + 1)%sizeOfTable

IN the case of "plus 3", the rehash is defined as:
rehash(pos) = (pos + 3) %sizeOfTable

General Formula:
rehash(pos) = (pos + skip)%sizeOfTable
**To ensure that the "skip" value visits all the slot of the table, LET THE TABLE BE A PRIME
NUMBERS

A variation of the linear probing idea is called QUADRATIC PROBING:
Instead of using a constant "skip" value, we use a rehash function that increment the hash value 
by 1, 3, 5, 7, 9, and so on. Meaning that id the first hash value is h, the successuve values 
are h+1, h+4, h+9, h+16, and so on. I.E., quadratic probing uses a skip consisting of successive 
perfect squares. 

An alternative method for handling the collision problem is to allow each slot to hold a 
reference to a collection (or chain) of items. 
CHAINING allows many items to exist at the same location in the hash table. WHen collisions
happen, the item is still placed in the proper slot of the hash table. As more and more items hash 
to the same location, the difficulty of searching for the item in the collection increases. 

"""

"""
IMPLEMENTING THE Map Abstract Data Type:
The mape abstract data type is defined as follows. The structure is an unordered collection of 
associations between a key and a data value. The keys in a map are all unique so that there is a 
one-one relationship between key and a value. 

Map(): create a new, empty map. It returns an empty map collection
put(key, val): add a new key-value pair to the map. if the key is already in the map then replace
				the old value with the new value
get(key): given a key, return a value stored in the map or None otherwise. 
del: delete the key-value pair from the map using a statement of the form: del map[key]
len(): return the number of key-value pairs stored in the map 
in: return True for a statement of the form 'key in map', if the given key is in the map, False
	otherwise

Benefits of a dictionary:
-lookup is very quick 

*It is important that the size be a prime number so that collision resloution algorithm can 
be as efficient as possible

"""
#Hashtable Class
class HashTable:
	def __init__(self):
		self.size = 11 
		self.slots = [None]*self.size
		self.data = [None]*self.size 

	def put(self, key, data):
		hashValue = self.hashfunction(key, len(self.slots))

		if self.slots[hashValue] == None:
			self.slots[hashValue] = key
			self.data[hashValue] = data
		else:
			if self.slots[hashValue] == key:
				self.data[hashValue] = data #replace
			else:
				nextslot = self.rehash(hashValue, len(self.slots))
				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot, len(self.slots))

				if self.slots[nextslot] == None: 
					self.slots[nextslot] = key
					self.data[nextslot] = data
				else:
					self.data[nextslot] = data #replace

	def hashfunction(self, key, size) : 
		return key%size

	def rehash(self, oldHash, size):
		return (oldHash+1)%size

	def get(self, key):
		startslot = self.hashfunction(key, len(self.slots))

		data = None
		stop = False
		found = False
		position = startslot

		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key: 
				found = True
				data = self.data[position]
			else: 
				position = self.rehash(position, len(self.slots))
				if position == startslot:
					stop = True
		return data

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		self.put(key, data)


x = HashTable()
x[54] = "cat"
x[26] = "dog"
x[93] = "lion"
x[17] = "tiger"
x[77] = "bird"
x[31] = "cow"
x[44] = "goat"
x[55] = "pig"
x[20] = "chicken"
print(x.slots)

x[20] = 'duck'
print(x[20])

"""
Analysis of Hashing:
BEst Case hashing: O(1) constant time search technique

LOad factor: lambda
If lambda is small, then there is a lower shance of collisions, meaning that items are more likely 
to be in slots where they belong.
If lambda is large, it means the table is filling up , then there are more and more collisions 
. MEANINF THE COLLISION resolution is more difficult, requiring more comparisons to find an empty 
slot. Chaining, increase collisions means an increased number of items on each chain. 

For a successful search using open addressing w/ linear probing, the average number of comparisons is 
approximately----> 1/2(1 + 1/(1-lambda))
Unsuccessful search gives --> 1/2( 1+(1/(1-lambda))^2)

If chaining is used, the average number of collisions is 1 + (lambda/2) for the successful case, 
and lambda comparisons if the search is unsuccessful
"""
