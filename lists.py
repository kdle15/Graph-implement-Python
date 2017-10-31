#lists are dynamics arrays

numberList = list()
numberList.append(1)
numberList = {1,2,3,4,4}
print(len(numberList))
print(numberList[1:3])
copy = numberList[:]

if 5 not in numberList:
    numberList.append(5)
if 1 in numberList: #0(n)
    numberList.remove(1) #0(n)
#remove at end
numberList.pop() #0(1)
#
min(numberList)
max(numberList)

numberList = range(5) #{0,1,2,3,4}
#random shuffle
import random
random.shuffle(numberList)

numberList.sort()















