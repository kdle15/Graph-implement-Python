numberSet = set()
#set in python are hash table
numberSet.add(1)

len((numberSet))
if 5 not in numberSet:
    numberSet.add(5)#0(1)
if 3 in numberSet:
    numberSet.remove(3)#0(1)
item = numberSet.pop()# takes out some arbirtrary items
#min and max
union = {1,2,3} | {3,4,5}
intersection = {1,2,3} & {3,4,5}
difference = {1,2,3} - {3,4,5}

if {1,2} <= {1,2,3}:
    print("subset")

pointSet = {{1,2},{3,5}}
#pointSet = {{1,2},{3,4}} inva;id
#set and list are unhashable
#frozenset()can
#frozenlist is tuple
