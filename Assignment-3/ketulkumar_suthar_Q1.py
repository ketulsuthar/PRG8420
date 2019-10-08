#!/usr/bin/env python

#Write a function called cube_not_equal(x,y,z,N).
#This function gets three integers x, y and z representing the dimensions of a cuboid along with an integer N.
#You have to return a set of all possible coordinates given by (i,j,k) on a 3D grid where the sum i+j+k of is not equal to N.
# Here, 0 ≤ i ≤ x, 0 ≤ j ≤ y, 0 ≤ k ≤ z.

def cube_not_equal(x,y,z,N):
    '''This function return all possible coordinates given by (i,j,k) on a 3D grid
    x,y,z,N : integer value
    '''
    int_type = 1
    try:
        if type(x) == type(int_type) and type(int_type) == type(int_type) and type(int_type) == type(int_type) and type(N) == type(int_type): #Check integer type
            return {(i,j,k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != N} # logic for getting all possible coordinates where i+j+k != N
        else:
            return None
    except:
        return None
