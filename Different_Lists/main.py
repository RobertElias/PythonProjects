
# Different types of lists app
# Defining lists
num_strings = ["15", "100", "55", "42"]
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\t\tSummary Table")

print("\nThe variable num strings is " + str(type(num_strings)) + ".")
print("It contains the elements: " + str(num_strings))
print("The element " + num_strings[0] +
      " is a " + str(type(num_strings[0])) + ".")

print("=====================================================================")
print("\nThe variable num integers is " + str(type(num_ints)) + ".")
print("It contains the elements: " + str(num_ints))
print("The element " + str(num_ints[0]) +
      " is a " + str(type(num_ints[0])) + ".")

print("=====================================================================")
print("\nThe variable num integers is " + str(type(num_floats)) + ".")
print("It contains the elements: " + str(num_floats))
print("The element " + str(num_floats[0]) +
      " is a " + str(type(num_floats[0])) + ".")

print("=====================================================================")
print("\nThe variable num integers is " + str(type(num_lists)) + ".")
print("It contains the elements: " + str(num_lists))
print("The element " + str(num_lists[0]) +
      " is a " + str(type(num_lists[0])) + ".")

#Sorting the lists
num_strings.sort()
num_ints.sort()
print("\nNow sorting num_strings and num_ints...")
print("Sorted num_strings: " + str(num_strings))

print("Sorted num_ints " + str(num_ints))