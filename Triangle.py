# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of the squares of two sides equals the square of the third side, then return 'Right'
      
    Defects fixed from the original version are marked with "FIX n" comments.
    """

    # FIX 1: the type check must come BEFORE any numeric comparison. Originally
    # it came after, so a string or None input raised a TypeError instead of
    # returning 'InvalidInput'.
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    # FIX 2: original compared "b <= b", which is always True, so every input
    # was rejected. It should be "b <= 0".
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly greater than the third side
    # otherwise the specified shape is not a triangle
    # FIX 3: original used differences (b - c, a - c) and compared them
    # incorrectly. Each side must be less than the sum of the other two.
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    # FIX 4: original checked "a == b and b == a", so c was never compared.
    if a == b and b == c:
        return 'Equilateral'
    # FIX 5: original used "* 2" instead of squares, and only treated c as the
    # hypotenuse. Check the Pythagorean relation for each side as hypotenuse.
    elif ((a ** 2) + (b ** 2) == (c ** 2)) or \
         ((a ** 2) + (c ** 2) == (b ** 2)) or \
         ((b ** 2) + (c ** 2) == (a ** 2)):
        return 'Right'
    # FIX 6: original repeated "a != b" and never compared a with c.
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'
