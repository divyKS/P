myTuple = ('pencil', 'sharpener') # immutable
checkTuple = ('pencil', 'sharpener')
print(id(myTuple) == id(checkTuple))
lameTuple = 1,2,3,4,5
print(type(lameTuple))
thirdTuple = myTuple + checkTuple
print(thirdTuple)
print(id(thirdTuple))
thirdTuple += (1,)
print(thirdTuple)
print(id(thirdTuple))
unsortedTuple = ('balloon', 'orange', 'rainbow', 'acorn')
print(id(unsortedTuple))
print(sorted(unsortedTuple))
print(id(sorted(unsortedTuple)))
print(max(unsortedTuple))
print(min(lameTuple))
print(sum(lameTuple))
for element in lameTuple:
    print(element)

print(id(lameTuple))
lameList = list(lameTuple)
lameList.append(6)
lameList[0]='apples'
lameTuple = tuple(lameList)
print(id(lameTuple))

results = ((1, 'AVS', 8.076), (8, 'HKS', 8.529), (11, 'DKS', 9.0001))
for i in results:
    print(str(i[0]) +'\t'+ i[1] +'\t'+ str(i[2]))
for i in range(0, len(results)):
    print(results[i][0])

a = 10
b = 20
(a, b) = (b, a)
print(a, b)

n = int(input('Enter your value of n: '))
inputList = []
print('Now enter your values')
while(n != 0):
    n = n - 1
    inputList.append(input())
inputTuple = tuple(inputList)
print('The minimum number is: ', min(inputTuple))
print('The maximum number is: ', max(inputTuple))

def priyanshu(*args):
    print(args)
    print(type(args))
    for argument in args:
        print(argument)

priyanshu(1,2,3,4,5)



class Kartik:
    def mc(self):
        print('thic')
    

class Divy:
    def mc(self):
        print('ds')


class Shinde(Kartik, Divy):
    def mc(self):
        print('avs')
    def confusion(self):
        self.mc()


priyanshu = Shinde()
priyanshu.confusion()

x = (i for i in range(3))
print(x)
print(type(x))
for i in x:
    print(i)
for i in x:
    print(i)
print(next(x))
print(next(x))
print(next(x))

import a
obj = a.A()
print(obj.__module__)
obj = Kartik()
print(obj.__module__)

