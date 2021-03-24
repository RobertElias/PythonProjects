#2. Write a Python program to multiplies all the items in a list.
def multiply_list(items):
    total = 1
    for x in items:
        total *= x
    return total

print(multiply_list([1,2,-8]))
print(multiply_list([1, 12, 8]))
print(multiply_list([11, 22, -8]))
