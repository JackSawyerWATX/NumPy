# Python program for
# Creation of Arrays
import numpy as np
 
# Creating a rank 1 Array
arr = np.array([1, 2, 3])
print("Array with Rank 1: \n",arr)
 
# Creating a rank 2 Array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arr)
 
# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr)

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)
 
# Printing a range of Array
# with the use of slicing method
sliced_arr = arr[:2, ::2]
print ("Array with first 2 rows and"
    " alternate columns(0 and 2):\n", sliced_arr)
 
# Printing elements at
# specific Indices
Index_arr = arr[[1, 1, 0, 3], 
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr)

a = np.array([[1, 2],
              [3, 4]])
 
# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])
               
# Adding 1 to every element
print ("Adding 1 to every element:", a + 1)
 
# Subtracting 2 from each element
print ("\nSubtracting 2 from each element:", b - 2)
 
# sum of array elements
# Performing Unary operations
print ("\nSum of all array "
       "elements: ", a.sum())
 
# Adding two arrays
# Performing Binary operations
print ("\nArray sum:\n", a + b)

x = np.array([1, 2])  
print("Integer Datatype: ")
print(x.dtype)         
 
# Float datatype
# guessed by Numpy
x = np.array([1.0, 2.0]) 
print("\nFloat Datatype: ")
print(x.dtype)  
 
# Forced Datatype
x = np.array([1, 2], dtype = np.int64)   
print("\nForcing a Datatype: ")
print(x.dtype)

arr1 = np.array([[4, 7], [2, 6]], 
                 dtype = np.float64)
                  
# Second Array
arr2 = np.array([[3, 6], [2, 8]], 
                 dtype = np.float64) 
 
# Addition of two Arrays
Sum = np.add(arr1, arr2)
print("Addition of Two Arrays: ")
print(Sum)
 
# Addition of all Array elements
# using predefined sum method
Sum1 = np.sum(arr1)
print("\nAddition of Array elements: ")
print(Sum1)
 
# Square root of Array
Sqrt = np.sqrt(arr1)
print("\nSquare root of Array1 elements: ")
print(Sqrt)
 
# Transpose of Array
# using In-built function 'T'
Trans_arr = arr1.T
print("\nTranspose of Array: ")
print(Trans_arr)

# NumPy Methods:
# all()
# any()
# take()
# put()
# apply_along_axis()
# apply_over_axes()
# argmin()
# argmax()
# nanargmin()
# nanargmax()
# amax()
# amin()
# insert()
# delete()
# append()
# around()
# flip()
# fliplr()
# flipud()
# triu()
# tril()
# tri()
# empty()
# empty_like()
# zeros()
# zeros_like()
# ones()
# ones_like()
# full_like()
# diag()
# diagflat()
# diag_indices()
# asmatrix()
# bmat()
# eye()
# roll()
# identity()
# arange()
# place()
# extract()
# compress()
# rot90()
# tile()
# reshape()
# ravel()
# isinf()
# isrealobj()
# isscalar()
# isneginf()
# isposinf()
# iscomplex()
# isnan()
# iscomplexobj()
# isreal()
# isfinite()
# isfortran()
# exp()
# exp2()
# fix()
# hypot()
# absolute()
# ceil()
# floor()
# degrees()
# radians()
# npv()
# fv()
# pv()
# power()
# float_power()
# log()
# log1()
# log2()
# log10()
# dot()
# vdot()
# trunc()
# divide()
# floor_divide()
# true_divide()
# random.rand()
# random.randn()
# ndarray.flat()
# expm1()
# bincount()
# rint()
# equal()
# not_equal()
# less()
# less_equal()
# greater()
# greater_equal()
# prod()
# square()
# cbrt()
# logical_or()
# logical_and()
# logical_not()
# logical_xor()
# array_equal()
# array_equiv()
# sin()
# cos()
# tan()
# sinh()
# cosh()
# tanh()
# arcsin()
# arccos()
# arctan()
# arctan2()