# List       =>  ordered, changeable, allow duplicates
# Tuple      =>  ordered, unchangeable, allow duplicates
# Set        =>  unordered, unindexed, no duplicates
# Dictionary =>  unordered, changeable, indexed, no duplicates


print("################ Lists  ###################")
print("")
#=========================================================================#
#======================= Lists ==========================================#
#=========================================================================#
thislist = [ "apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist)
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[3:])
print(thislist[:4])
print(thislist[-4:-1])

# Change item value
thislist[2] = "blackcurrant"
print(thislist)

## Loop through a list
for x in thislist:
    print(x)

# Check if item exists
if "apple" in thislist:
    print("Yes, 'apple'  is in the fruits list")    

# List length
print(len(thislist))    

# Add items
thislist.append("orange")
print(thislist)

# Add items at the specified index
thislist.insert(1,"orange")
print(thislist)

# Remove item 
thislist.remove("banana")
print(thislist)

# pop() removes the specified index(or last item if index is not specified)
thislist.pop()
print(thislist)

# del removes the specified index
del thislist[0]
print(thislist)

#  del thislist =>  delete the list completely

# thislist.clear()
print(thislist)

# Copy a list
myList = thislist.copy()
print(myList)

myList =  list(thislist)
print(myList)

# Join Two List

list1 = ["a","b","c"]
list2 = [1,2,3]
list3 =  list1 + list2
print(list3)

list1.extend(list2)
print(list1)

# list() constructor
listX = list(("apple","banana","cherry"))
print(listX)


### List methods ###
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

print("")
print("################ Tuples ###################")
print("")
#=========================================================================#
#======================= Tuples ==========================================#
#=========================================================================#

tupleA = ("apple","banana","cherry")
print(tupleA)
print(tupleA[1]) # returns "apple"
print(tupleA[-1]) # returns "cherry"
print(tupleA[:1])

# Tuples are immutable or unchangeable to modify tuples convert to list then back to tuple
tupleB = ("Kane","Bale","Son","Moura")
print(tupleB)
listX = list(tupleB)
listX[1] = "Dele"
tupleC = tuple(listX)
print(tupleC)

# Loop through tuple
for x in tupleC:
    print(x)

# Check item exist
if "Son" in tupleC:
    print("Son is in the squad Today")

# Tuple length
print(len(tupleC))  

#### Tuple methods ###
# count() 
# index()

print("")
print("################ Sets  ###################")
print("")
#=========================================================================#
#======================= Sets ==========================================#
#=========================================================================#
# sets are unordered and unindexed.
setA = {"apple","banana","cherry"}
print(setA)

# Access items in a set
for x in setA:
    print(x)

# Check item in tuple
print("banana" in setA)    

# Add items 
# add one item use add()
# add more than one item user update()

setA.add("orange")
print(setA)

setA.update(["mango","grapes","orange"])
print(setA)

# Length of set 
print(len(setA))

# Remove item 
setA.remove("banana") # if item is not found will raise an error
print(setA)
# setA.remove("banana")

setA.discard("banana") # if item is not found will not raise an error
print(setA)

setA.pop()
print(setA)

# empty set 
setA.clear()
print(setA)

#Join two sets use union()
set1 ={"a","b","c"}
set2 ={1,2,3}
set3  =set1.union(set2)
print(set3)

### Set Methods ###
# Method	                    Description

# add()	                        => Adds an element to the set
# clear()	                    => Removes all the elements from the set
# copy()	                    => Returns a copy of the set
# difference()	                => Returns a set containing the difference between two or more sets
# difference_update()	        => Removes the items in this set that are also included in another, specified set
# discard()	                    => Remove the specified item
# intersection()	            => Returns a set, that is the intersection of two other sets
# intersection_update()	        => Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                => Returns whether two sets have a intersection or not
# issubset()	                => Returns whether another set contains this set or not
# issuperset()	                => Returns whether this set contains another set or not
# pop()	                        => Removes an element from the set
# remove()	                    => Removes the specified element
# symmetric_difference()	    => Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	=> inserts the symmetric differences from this set and another
# union()	                    => Return a set containing the union of sets
# update()	                    => Update the set with the union of this set and others


print("")
print("################ Dictionary  ###################")
print("")
#=========================================================================#
#======================= Dictionary ==========================================#
#=========================================================================#
# unordered,chnageable, indexed
dictA = {"brand":"Subaru","model":"Impreza G4", "year":2014 ,"month":2, "mileage":78000,"color":"Pearl White"}
print(dictA)

x = dictA["model"]
print(x)

x = dictA.get("model")
print(x)

# Change values
dictA["year"] = 2013
print(dictA)

# loop through dictionary keys
for x in dictA:
    print(x)

# return values
for  x in dictA:
    print(dictA[x])

# use values() 
for x in dictA.values():
    print(x)    

# Loop through keys and values by using items()
for x, y in dictA.items():
    print(x, y)

# Check if key Exists
if "model" in dictA:
    print("Yes  , \" Model\" is one of the keys in this car specification dictionary")    

# Dictionary length
print(len(dictA))    

# Adding item to dictionary
dictA["body"] = "sedan"
print(dictA)

# Remove item  using pop()
dictA.pop("model")
print(dictA)
print(len(dictA))

# popitem() removes last inserted item (version 3.7 below, a random item is removed)
dictA.popitem()
print(dictA)

# copy dictionary 
dictB =  dictA.copy()
print(dictB)

# or
dictB  = dict(dictA)
print(dictB)

# Dictionary methods
# Method	Description
# clear()	     => Removes all the elements from the dictionary
# copy()	     => Returns a copy of the dictionary
# fromkeys()	 => Returns a dictionary with the specified keys and value
# get()	         => Returns the value of the specified key
# items()	     => Returns a list containing a tuple for each key value pair
# keys()	     => Returns a list containing the dictionary's keys
# pop()	         => Removes the element with the specified key
# popitem()	     => Removes the last inserted key-value pair
# setdefault()	 => Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	     => Updates the dictionary with the specified key-value pairs
# values()	     => Returns a list of all the values in the dictionary


print(dictA.keys())