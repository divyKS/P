likes = {"color": "blue", "fruit": "apple", "pet": "dog", "key1": "value1", "key2": "value2", "key3": "value3"}
print(likes.keys())
print(likes.values())
print(likes.items())
print(likes.pop("key1")) #removes from the dict too permanently
print(likes.popitem()) #removed the last pair permanently
print(likes)
print(('color', 'blue') in likes.items())

myDict = {"color": "blue", "fruit": "apple", "pet": "dog", 1: "value1", 2.33: "value2", (1,): "value3"}
myDict['myName'] = 'DivyKS'

for i in myDict:
    print(i)

myDict.update(likes)#diff keys ones are added to myDict
print(myDict)
myDict.clear()
print(myDict.copy())
print(myDict.get(1)) 
print(myDict[1])

# creating dict using dict constructor
weird = dict(Key1="value1", key2="value2", key3="value3")
weird[4] = "value4" # couldn't do this above
print(weird)

weirder = dict(zip(("key1", "key2", 3), ("value1", "value2", "value3")))
print(weirder)

wtf = dict((("key1", "value1"), ("key2", "value2"), ("key3", "value3")))
print(wtf)

waffle = dict([["key1", "value1"], ["key2", "value2"], ["key3", "value3"]])
print(waffle)

del(waffle["key1"])
print(waffle)
del(waffle)
print(waffle)

answer = True
while answer:
    found = False
    valueToCheck = input('Enter the value which you want to find(reverse lookup): ')
    for key in likes:
        if(likes[key] == valueToCheck):
            print('The key for this value has been found: ', key)
            found = True
            break
    if(not found):
        print('This value not found')
    answer = input('DO you want to check for for another value?True/False: ') == 'True'
    
