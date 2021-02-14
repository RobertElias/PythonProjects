print("Welcome to the Letter Counter App")

# Get user input
name = input("What is your name: ").title().strip()
print("Hello, " + name + "!")

print("I will now count the number of times that a specific letter occurs in this message.")

message = input("\nPlease enter a message: ")
letter = input("Which letter would you like to count the occurences of: ")

message = message.lower()
letter = letter.lower()

letter_count = message.count(letter)

print("\n" + name + ", your message has " + str(letter_count) + " " + letter + "'s in it.")