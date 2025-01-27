myList = list() # []
mydict = dict()# {}
mySet = set()

#List
myList.append(5)
myList + [1,2,2,3,122,4,5,2,1,534,55]

#Dictionary methods
mydict[1] = "One"
mydict.update({2:"Two",3:"Three",4:"Four"})
print("Dict_keys : ",mydict.keys())
print("Dict_values : " , mydict.values())
print("Dict_items : ",mydict.items())


#Set  and set methods
mySet.add(5)
ListToSet = set(myList)

union = mySet.union(ListToSet)
intersection = mySet.intersection(ListToSet)
difference = mySet.difference(ListToSet)

print("List ",myList)
print("mydict : ",mydict)
print("mySet : ",mySet)
print("Union :", union)
print("intersection :",intersection)
print("difference :", difference)