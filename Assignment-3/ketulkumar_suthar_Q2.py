#!/usr/bin/env python


#An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
#If a new entry overwrites an existing entry, the original insertion position is left unchanged.
#You have a list of N items together with their prices that consumers bought on a particular day.
#Your task is to print each item_name and net_price in order of its first occurrence.
#item_name = Name of the item.
#net_price = Quantity of the item sold multiplied by the price of each item.
#Input: The first line contains the number of items, and the next N lines contains the item's name and price, separated by a space.
#Output: Print the item_name and net_price in order of its first occurrence.

from collections import OrderedDict


int_type=1
item = OrderedDict() # Create ordered dictionary
try:
    no_of_items = int(input())
    while no_of_items > 0: #interate upto no_of_items
        item_list = input().split() # split input and make item list
        if type(int(item_list[-1])) == type(int_type):
            item[' '.join(item_list[:-1])] = item.get(' '.join(item_list[:-1]),0) + int(item_list[-1])
            no_of_items -= 1
except Exception as e :
    print("Invalid argument.")

for key,value in item.items():
    print(key,value)
