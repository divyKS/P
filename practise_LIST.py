myName = 'DKS'
print(id(myName))
myOtherName = 'DKS'
print(id(myOtherName))
myOtherName += '_!'
print(id(myOtherName))
print(id('DKS'))

print(type('d' not in myName))

text = '   abcde   '
print(text.upper().strip().replace('AB', 'zy').split('CD'))

myList = ['i', 'am', 34]
print(myList.pop())
print(myList)
print(myList.pop(0))
print(myList)

checkList = ['i', 'am', 34] # hence mutable
print(id(myList))
print(id(checkList))
herList = ('apples', 'peaches')
hisList = ['cake', 'coke']
print(id(myList))
myList.append('ds')
print(id(myList))
print(id(myList.copy()))
myList.extend(herList)
print(myList)
print(myList.index(33))
myList.reverse() # returns nothing, None would be printed
print(myList)
print(myList, end=' ')
print('apples??')
print(myList + hisList) #same as extend, but works when both are lists
myList.append(hisList)
print(myList)
myList.extend(herList) # extend works with tuples too
print(myList)
del(hisList)
print(hisList)
