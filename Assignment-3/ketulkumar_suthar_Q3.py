#!/usr/bin/env python

#Write a function called print_upto_N(N) which prints all the numbers from 1 through N without using any string methods,
#as the following: 12…N Note that "…" represents the values in between.


def print_upto_N(N):
    '''This function print 1 to N number without using any string method
    N: integer number
    '''
    int_type=99
    if type(N) == type(int_type): # Check enter number is integer
        for i in range(1,N+1):
          print(i,end=' ') # use end=' ' for print number in single line.
    else:
        print("Number should be numeric.")
