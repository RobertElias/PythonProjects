print("Welcome to the binary/hexadecimal converter app.")

# Get user input and generate list
max_value = int(input(
    "\nCompute binary and hexadecimal values up to the following decimal number: "))
decimal = list(range(1, max_value + 1))
# print(decimal)
binary = []
hexadecimal = []

for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print("Generating lists...Complete!")

# Get slicing index from user
print("\nUsing slices, we will now show a portion of each list.")
lower_range = int(input("What decimal nujmber would you like to start at: "))
upper_range = int(input("What decimal nujmber would you like to stop at: "))

# Slice each list individually
print("\nDecimal values from " + str(lower_range) +
      " to " + str(upper_range) + ".")
for num in decimal[lower_range-1:upper_range]:
    print(num)

print("\nBinary values from " + str(lower_range) +
      " to " + str(upper_range) + ".")
for num in binary[lower_range-1:upper_range]:
    print(num)

print("\nHexadecimal values from " + str(lower_range) +
      " to " + str(upper_range) + ".")
for num in hexadecimal[lower_range-1:upper_range]:
    print(num)

#outpout list to screen
input("\nPress enter to see all values from 1 to " + str(max_value)+ ".")
print("Decimal----Binary----Hexadecimal")
print("-----------------------------------")

for d, b, h in zip(decimal, binary, hexadecimal):
    print(str(d)+ "----"+ str(b) + "----" +str(h))