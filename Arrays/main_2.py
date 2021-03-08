#2. Write a Python program to append a new item to the end of the array.

from array import *
array_num = array("i", [1,3,5,3,7,1,9,3])
print("Original array: " + str(array_num))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))