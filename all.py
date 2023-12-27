text = '1001'
print(int(text, 2))
print(float(90))

char = 'a'
print(ord(char))
print(chr(97))
print(chr(65))
print(hex(230)) # coverts int to hexadecimal string
print(oct(89)) # coverts int to octal string

str = 'bananas'
print(tuple(str))
print(set(str))
print(list(str))

myTuple = (('a', 1) ,('f', 2), ('g', 3)) # can be list of lists
print(dict(myTuple))

print(complex(1, 2)) #returns a complex class object

def myFunction(name='DS'):
    print(name)
myFunction('DKS')
myFunction()

# keyword arguments
def person_name(first_name,second_name): 
    print(first_name+second_name) 

person_name(second_name="Babu",first_name="Ram")

print(bool(""))
print(bool("beffdg"))
print(bool(0))
print(bool(1))
print(bool(1345))
print(bool(tuple)) #just should be empty
print(bool(list))
print(bool(dict))

# these are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

print(isinstance(5, int))
print(isinstance({1:"one", 2:"two", 3:"three"}, dict))
x = isinstance("Hello", (float, int, str, list, dict, tuple)) # any from that

name = 'divy'
print(name.find('i').__doc__)
marks = 8.3
result = 'pass' if marks > 7 else 'fail'
print(result)