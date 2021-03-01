print("Welcome to the Letter Counter App")

# Get user input
name = input("What is your name: ").title().strip()
print("Hello, " + name + "!")

print("I will now count the number of times that a specific letter occurs in this message.")

# store the message and letter inputs in variables
message = input("\nPlease enter a message: ")
letter = input("Which letter would you like to count the occurences of: ")

# convert message and letter input to lower case
message = message.lower()
letter = letter.lower()

# create letter_count variable to use .count(letter)
letter_count = message.count(letter)

# print message
print("\n" + name + ", your message has " +
      str(letter_count) + " " + letter + "'s in it.")
