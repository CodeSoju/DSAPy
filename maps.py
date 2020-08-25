"""
The concept of a map os already built-in data type called a dictionary. A dictionary contains
key-value pairs. Dictionaries might soon 

the keys() method of a dictionary object returns a list of all the keys used in the dictionary
in arbitrary order(if you want it sorted, just apply the sorted() function to it. )
"""

tel = {'jack' : 4098, 'sape' : 4139}
tel['guido'] = 4127
#print(tel)
#print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
#print(tel)

#print("Value : %s" % str(tel.keys()))

dicA = {x: x**2 for x in (2, 4, 6)}
#print(dicA)

#When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments
#print(dict(sape=4139, guido=4127, jack=4098))

# LOOPING TECHNIQUES: 
# When looping through a sequence, the position index and corresponding value can be retrieved 
# at the same thing using the enumerate() function
"""
Enumerate Function
enumerate(sequence, start=0):
return an enuermate object. "sequence" must be a sequencem an iterator, or some other object
which supports iteration. 
"""
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons, start =1 )))

"""
This is equal to:
def enumerate(sequence, start = 0):
	n = start
	for elem in sequence:
		yield n, elem
		n += 1

"""

"""
Iterables

When you create a list, you can read its items one by one, and it's called iteration :
"""

mylist = [1, 2, 3]
for i in mylist:
	print(i)

list2 = [x*x for x in range(3)]
for i in list2:
	print(i)


"""
Generators:
Generators are iterators, but you can only iterate over them once. Reason being is that they 
do not share all the values in memory, they generate the values on the fly
"""
myGenerator = (x*x for x in range(3))
for i in myGenerator:
	print(i)

"""
Yield: a keywor that is used like return, except the function will return a generator 
"""

"""
TO understand 'yield', you must understand that whne you call the function, the code you 
have written in the function body does not run. 

The first time the for calls the generator object created from your function
"""