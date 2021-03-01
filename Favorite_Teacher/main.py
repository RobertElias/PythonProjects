print("Welcome to the Favorite Teachers Program")

fav_teachers = []

#Get user input
fav_teachers.append(input("Who is your first favorite teacher: ").title())
fav_teachers.append(input("Who is your second favorite teacher: ").title())
fav_teachers.append(input("Who is your third favorite teacher: ").title())
fav_teachers.append(input("Who is your fourth favorite teacher: ").title())


#Summary of list

print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("You favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("You favorite teachers in reverse are: " + str(sorted(fav_teachers, reverse=True)))
print("\nYour top Two favorite teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teachers is: " + fav_teachers[-1])

print("You have a total of: " + str(len(fav_teachers)) + " favorite teachers.")

#Insert a new favorite teacher

fav_teachers.insert(0, input("\nOops, " + fav_teachers[0] + " is no longer you first favorite teacher. Who is your new Favorite Teacher: ").title())

#Summary of list

print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("You favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("You favorite teachers in reverse are: " +
      str(sorted(fav_teachers, reverse=True)))
print("\nYour top Two favorite teachers are: " +
      fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " +
      fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teachers is: " + fav_teachers[-1])

print("You have a total of: " + str(len(fav_teachers)) + " favorite teachers.")


#Remove a specific teacher
fav_teachers.remove(input("\nYou decide you no longer like a teacher. Who do we remove form the list: ").title())

#Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("You favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("You favorite teachers in reverse are: " +
      str(sorted(fav_teachers, reverse=True)))
print("\nYour top Two favorite teachers are: " +
      fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " +
      fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teachers is: " + fav_teachers[-1])
print("You have a total of: " + str(len(fav_teachers)) + " favorite teachers.")
