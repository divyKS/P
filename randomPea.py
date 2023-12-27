# pip install pandas
# import pandas
# file = pandas.read_csv('erre.csv')
# fileNew = pandas.red_excel('sdcd.xlsx')

try:
    result = 10/0
except ZeroDivisionError as e:
    # ZeroDivisionError
    #KeyError
    #IndexError
    #ValueError
    print(e)
    print(type(e))

from abc import ABC, abstractmethod
class LO(ABC):
    @abstractmethod
    def scream():
        pass

class PO(LO):
    def __init__(self):
        pass
    def scream(self):
        print('Mai to abstraction hu')

myObj = PO()
myObj.scream()

try:
    result = 10 / 0  # Example of a division by zero
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No exception occurred.")
finally:
    print("This code always runs.")

import random
print(random.randint(0,100))