from typing import Counter
from src import *

var = input('Enter number: ')

counter = 0

for i in cd:
    if counter == int(var):
        break
    print(counter+1, cd[counter]['id'], cd[counter]
          ['symbol'], cd[counter]['market_cap'])
    counter += 1
