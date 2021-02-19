# Roster application

print("Welcome to the Basketball Roster Program.")

#Get the user input and define the roster
roster = []
player = input("\nWho is your point guard: ").title()
roster.append(player)
player = input("Who is your shooting guard: ").title()
roster.append(player)
player = input("Who is your small forward: ").title()
roster.append(player)
player = input("Who is your power forward: ").title()
roster.append(player)
player = input("Who is your center: ").title()
roster.append(player)
#Dispaly Roster
print("\n\tYour starting 5 for the upcoming basketball season")
print("\T\TPoint Guard:\t\t" + roster[0])
print(roster)
