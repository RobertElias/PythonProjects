#11. Write a Python program to remove a specified item using the index from an array.

from array import *
array_num = array('i', [1,3,5,7,9])
print("Original array: "+str(array_num))
print("Remove the third item from the array:")
array_num.pop(2)
print("New array: "+str(array_num))